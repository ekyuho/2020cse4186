import requests
import json

with open("url_call.txt") as f: 
    lines = f.read().splitlines()

i = 1
log = {"ok":{},"insufficient":{}, "param":{}, "json":{}, "timeout":{}, "404":{}}
given = {"season":"spring", "flowers":"brooming", "iam":"happy", "howmuch":"very"}
expected = {"stuno", "time", "ip", "email"}
for url in lines:
    parm = "?"
    amp = ""
    for x in given: 
        parm += "%s%s=%s"%(amp,x,given[x])
        amp = '&'

    print("%d. %s"%(i, url))
    for method in {"get", "post"}:
        try:
            if method == "get": 
                print("  get() ->  ", end=" ")
                r = requests.get(url+parm, timeout=5)
            elif method == "post": 
                print("  post() -> ", end=" ")
                r = requests.post(url, data=given, timeout=5)
    
            if r.status_code == 404: 
                log["404"]["%s-%s"%(url,method)] = " not found"
                print("404 not found")
            else:
                try:
                    j = json.loads(r.text)

                    if not set(given).issubset(j):
                        log["param"]["%s-%s"%(url,method)] = " "+r.text
                        print("incorrect param return %s"%r.text[:20])
                    elif not expected.issubset(j):
                        log["insufficient"]["%s-%s"%(url,method)] = " "+r.text
                        print("insufficient params %s"%r.text[:20])                    
                    else:
                        log["ok"]["%s-%s"%(url,method)] = " "+r.text
                        print("--> %s"%r.text[:20])
                except json.JSONDecodeError:
                    log["json"]["%s-%s"%(url,method)] = "json decode error: "+ r.text
                    print(" err: json decode: "+ r.text[:20])
        except:
            log["timeout"]["%s-%s"%(url,method)] = " timeout error"
            print(" timeout")
        
    i += 1
    
def save(reason):
    with open("url_all_result_%s.txt"%reason, "w") as f:
        k = sorted(log[reason].keys())
        for x in log[reason]: 
            print(x, json.dumps(log[reason][x]).replace('\\','')[:80], file=f)
    print("done %s"%reason)
    
for x in log: save(x)
