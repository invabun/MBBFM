import urllib.request, re

req = urllib.request.Request('https://ahbundance.blogspot.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as r:
    html = r.read().decode('utf-8')

# Find lh googleusercontent URLs (Google profile photos)
lh = re.findall(r'https://lh\d\.googleusercontent\.com/[^"\'\s]+', html)
print("lh photos:", lh[:10])

# Find any profile-image related img tags
profile = re.findall(r'<img[^>]+class="[^"]*profile-photo[^"]*"[^>]*>', html)
print("profile imgs:", profile[:5])

# Find blogger profile image widget
widget = re.findall(r'<img[^>]+/photo\.jpg[^>]*>|https://[^"\']+/photo\.jpg', html)
print("photo.jpg:", widget[:5])
