import requests
import json

#pur your url here
#lines = ['http://ec2-3-21-37-105.us-east-2.compute.amazonaws.com:8000/input?device_id=99&temperature_value=29.99&sequence_number=456']
lines = ""

with open("url_call2.txt", encoding='utf8') as f: 
    lines = f.read().splitlines()

i = 1
for url in lines:
    print()
    i += 1
    if not ('ZZZZZ' in url):
        print('%d. ZZZZZ 가 URL에 없습니다: %s'%(i, url))
        print('skip')
        continue

    url = url.replace('ZZZZZ', '99')  # 99  or empty
    print('%d. call %s'%(i, url))
    
    try:
        r = requests.get(url, timeout=5) 
        if r.status_code == 404: 
            print("404 not found")
            continue
    except:
        print("Error ")
        continue

    try:
        j = json.loads(r.text)
    except json.JSONDecodeError:
        print(" err: json decode: "+ r.text[:80])
        continue
               
    print('success: %d records: %s'%(len(j), json.dumps(j)[:80]))
