#!/usr/bin/env python3
"""
Import all Blogspot posts from ahbundance.blogspot.com to Jekyll _posts folder.
"""
import json
import re
import os
import urllib.request
from datetime import datetime

POSTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_posts")
os.makedirs(POSTS_DIR, exist_ok=True)

def fetch_all_posts():
    all_entries = []
    start = 1
    while True:
        url = f"https://ahbundance.blogspot.com/feeds/posts/default?max-results=50&start-index={start}&alt=json"
        print(f"Fetching posts {start} to {start+49}...")
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        feed = data.get("feed", {})
        entries = feed.get("entry", [])
        if not entries:
            break
        all_entries.extend(entries)
        total = int(feed.get("openSearch$totalResults", {}).get("$t", 0))
        print(f"  Got {len(entries)} posts. Total so far: {len(all_entries)} / {total}")
        if len(all_entries) >= total:
            break
        start += 50
    return all_entries

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    text = text.strip("-")
    # limit length
    return text[:60] if text else "post"

def get_post_url_slug(entry):
    for link in entry.get("link", []):
        if link.get("rel") == "alternate":
            href = link.get("href", "")
            # extract slug from URL
            m = re.search(r"/(\d{4})/(\d{2})/(.+?)\.html", href)
            if m:
                return m.group(3)
    return None

def convert_entry(entry):
    title = entry.get("title", {}).get("$t", "Untitled")
    published = entry.get("published", {}).get("$t", "")
    content_html = entry.get("content", {}).get("$t", "")
    categories = [c.get("term", "") for c in entry.get("category", []) if "blogger.com/atom/ns#" in c.get("scheme", "")]

    # Parse date
    try:
        dt = datetime.fromisoformat(published[:19])
        date_str = dt.strftime("%Y-%m-%d")
    except Exception:
        date_str = "2000-01-01"

    # Get URL slug
    url_slug = get_post_url_slug(entry)
    if not url_slug:
        url_slug = slugify(title) or date_str

    filename = f"{date_str}-{url_slug}.md"
    # sanitize filename
    filename = re.sub(r'[<>:"/\\|?*]', "-", filename)

    # Build front matter
    # Escape quotes in title
    title_escaped = title.replace('"', '\\"')
    tags_str = ""
    if categories:
        tags_list = "\n".join(f'  - "{t}"' for t in categories if t)
        tags_str = f"tags:\n{tags_list}\n"

    front_matter = f"""---
title: "{title_escaped}"
date: {date_str}
{tags_str}---

"""
    # Keep HTML content as-is (Jekyll renders HTML in markdown files)
    content = front_matter + content_html

    return filename, content

def main():
    entries = fetch_all_posts()
    print(f"\nConverting {len(entries)} posts...")
    success = 0
    for entry in entries:
        try:
            filename, content = convert_entry(entry)
            filepath = os.path.join(POSTS_DIR, filename)
            # handle duplicate filenames
            base, ext = os.path.splitext(filepath)
            counter = 1
            while os.path.exists(filepath):
                filepath = f"{base}-{counter}{ext}"
                counter += 1
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            success += 1
        except Exception as e:
            print(f"  ERROR: {e} for entry: {entry.get('title',{}).get('$t','?')}")
    print(f"\nDone! {success}/{len(entries)} posts saved to {POSTS_DIR}")

if __name__ == "__main__":
    main()
