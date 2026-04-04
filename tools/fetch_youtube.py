"""Fetch YouTube RSS and generate _data/youtube.yml for Jekyll."""
import os
import urllib.request
import xml.etree.ElementTree as ET

CHANNEL_ID = 'UC4bgvCbUSHs3p-SNLjZL9mQ'
FEED_URL = f'https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}'
OUT = os.path.join(os.path.dirname(__file__), '..', '_data', 'youtube.yml')

os.makedirs(os.path.dirname(OUT), exist_ok=True)

req = urllib.request.Request(FEED_URL, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, timeout=15) as r:
    xml_data = r.read()

ns = {
    'atom': 'http://www.w3.org/2005/Atom',
    'yt': 'http://www.youtube.com/xml/schemas/2015',
    'media': 'http://search.yahoo.com/mrss/',
}

root = ET.fromstring(xml_data)
videos = []

for entry in root.findall('atom:entry', ns):
    vid = entry.find('yt:videoId', ns).text
    title = entry.find('atom:title', ns).text
    published = entry.find('atom:published', ns).text[:10]  # YYYY-MM-DD
    link_el = entry.find('atom:link', ns)
    url = link_el.get('href')
    thumb = f'https://i.ytimg.com/vi/{vid}/mqdefault.jpg'

    media_group = entry.find('media:group', ns)
    stats = media_group.find('media:community/media:statistics', ns) if media_group else None
    views = int(stats.get('views', 0)) if stats is not None else 0

    videos.append({
        'id': vid,
        'title': title,
        'date': published,
        'url': url,
        'thumbnail': thumb,
        'views': views,
    })

with open(OUT, 'w', encoding='utf-8') as f:
    for v in videos:
        f.write(f"- id: {v['id']}\n")
        f.write(f"  title: \"{v['title'].replace('\"', '\\\"')}\"\n")
        f.write(f"  date: \"{v['date']}\"\n")
        f.write(f"  url: \"{v['url']}\"\n")
        f.write(f"  thumbnail: \"{v['thumbnail']}\"\n")
        f.write(f"  views: {v['views']}\n")

print(f'Saved {len(videos)} videos to {OUT}')
