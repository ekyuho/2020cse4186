import requests
import json

expected = {'device_id', 'status', 'time'}

#pur your url here
#lines = ['http://ec2-3-21-37-105.us-east-2.compute.amazonaws.com:8000/input?device_id=99&temperature_value=29.99&sequence_number=456']
lines = ""

if lines == "":
    with open("url_call.txt") as f: 
        lines = f.read().splitlines()

i = 0
for url in lines:
    i += 1
    if not (('XXXXX' in url) and ('YYYYY' in url)):
        print('%d. XXXXX 와 YYYYY가 URL에 없습니다: %s'%(i, url))
        print('skip')
        continue

    url = url.replace('XXXXX', '99').replace('YYYYY', '29.99')
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
        print(" err: json decode: "+ r.text)
        continue

    try:
        check = expected.issubset(j)
    except:
        print("return value not proper: "+ r.text)
        continue;
       
    if not check:
        print("insufficient items %s"%r.text)
        continue
               
    print('success: %s'%r.text)
