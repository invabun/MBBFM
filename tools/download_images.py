#!/usr/bin/env python3
"""
Download all images from imported blog posts and update image URLs to local paths.
"""
import os
import re
import urllib.request
import hashlib
import time
from pathlib import Path

POSTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_posts")
ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "img", "blog")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Match img src and href pointing to blogger/youtube images
IMG_PATTERN = re.compile(
    r'(src|href)="(https?://(?:blogger\.googleusercontent\.com|[0-9]+\.bp\.blogspot\.com)[^"]+)"',
    re.IGNORECASE
)

def url_to_filename(url):
    # Use hash of URL as unique filename, keep extension
    h = hashlib.md5(url.encode()).hexdigest()[:12]
    # Try to get extension from URL
    clean = url.split("?")[0].split("#")[0]
    ext = os.path.splitext(clean)[-1].lower()
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"):
        ext = ".jpg"
    return h + ext

def download_image(url, dest_path):
    if os.path.exists(dest_path):
        return True
    try:
        # Use smaller thumbnail version if available (replace /s1600/ with /s800/)
        download_url = re.sub(r'/s\d{3,4}(-c)?/', '/s800/', url)
        req = urllib.request.Request(download_url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        with open(dest_path, "wb") as f:
            f.write(data)
        return True
    except Exception as e:
        # Try original URL
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = resp.read()
            with open(dest_path, "wb") as f:
                f.write(data)
            return True
        except Exception as e2:
            print(f"  SKIP {url[:80]}... ({e2})")
            return False

def process_post(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    urls_found = IMG_PATTERN.findall(content)
    if not urls_found:
        return 0

    url_map = {}
    for attr, url in urls_found:
        if url in url_map:
            continue
        filename = url_to_filename(url)
        dest_path = os.path.join(ASSETS_DIR, filename)
        if download_image(url, dest_path):
            url_map[url] = f"/assets/img/blog/{filename}"
        time.sleep(0.05)  # be polite

    if not url_map:
        return 0

    # Replace URLs in content
    def replacer(m):
        attr, url = m.group(1), m.group(2)
        new_url = url_map.get(url, url)
        return f'{attr}="{new_url}"'

    new_content = IMG_PATTERN.sub(replacer, content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return len(url_map)

def main():
    posts = sorted(Path(POSTS_DIR).glob("*.md"))
    print(f"Processing {len(posts)} posts...")
    total_images = 0
    for i, post in enumerate(posts, 1):
        count = process_post(str(post))
        if count:
            print(f"[{i}/{len(posts)}] {post.name}: {count} images")
            total_images += count
        elif i % 50 == 0:
            print(f"[{i}/{len(posts)}] ...")
    print(f"\nDone! Downloaded {total_images} images to assets/img/blog/")

if __name__ == "__main__":
    main()
