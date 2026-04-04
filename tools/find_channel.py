import urllib.request, re
req = urllib.request.Request('https://www.youtube.com/@MBBFM', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
r = urllib.request.urlopen(req, timeout=10)
html = r.read().decode('utf-8')
r.close()
ids = set(re.findall(r'UC[a-zA-Z0-9_-]{22}', html))
print("Channel IDs found:", ids)
