import urllib.request

ids = [
    'UCt-70zfL_dOd_KCk36SZQrw',
    'UCk7atIy5ib2cJ76T_hb-dIg',
    'UCMC3Y6aW7206EzjlsEPkytg',
    'UCQlVT5D3AGQ70G25voXIfVQ',
    'UCUuZH4RIyJ8IEZHeQ6aRUcv',
    'UCDEl6vmAnie6fY6Z3cRisyF',
    'UCN6IfUgkn63t8ZwkcMGyvdg',
    'UC4bgvCbUSHs3p-SNLjZL9mQ',
    'UCMwFn3Pg2z66LwJFKmw4O15',
    'UCxK7FAWf14v3o4y8FPOAGx4',
    'UCNeQ9T5rGfaIt83mvIexKPo',
]

for cid in ids:
    url = f'https://www.youtube.com/feeds/videos.xml?channel_id={cid}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = r.read().decode('utf-8')[:500]
            if 'MBBFM' in data or 'mbbfm' in data.lower() or '少沣' in data:
                print(f"MATCH: {cid}")
                print(data[:300])
                print("---")
            elif '<title>' in data:
                import re
                title = re.findall(r'<title>(.*?)</title>', data)
                print(f"{cid}: {title[:2]}")
    except Exception as e:
        print(f"{cid}: {e}")
