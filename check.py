import requests
import json
from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)

lines = "http://ec2-34-235-96-225.compute-1.amazonaws.com:8000"

log = {"ok":{},"insufficient":{}, "param":{}, "json":{}, "timeout":{}, "404":{}}
given = {"season":"spring", "flowers":"brooming", "iam":"happy", "howmuch":"very"}
expected = {"stuno", "time", "ip", "email"}

def main(url):
    s = "\ngot url "+ url
    parm = "?"
    amp = ""
    for x in given:
        parm += "%s%s=%s"%(amp,x,given[x])
        amp = '&'

    print("%s"%(url))
    for method in {"get", "post"}:
        try:
            if method == "get":
                print("\nGET:  -> ", end=" ")
                s += "\n\nGET:  -> "
                r = requests.get(url+parm, timeout=5)
            elif method == "post":
                print("\nPOST: -> ", end=" ")
                s += "\n\nPOST: -> "
                r = requests.post(url, json=given, timeout=5)

            if r.status_code == 404:
                log["404"][url] = method + "  "+" not found"
                print("\nERROR: non existing path in URL ")
                s += "\nERROR: non existing path in URL "
            else:
                print("(HTTP OK) "+r.text)
                s += "(HTTP OK) "+r.text +'\n'
                try:
                    j = json.loads(r.text)

                    if not set(given).issubset(j):
                        log["param"][url] = method + "  "+r.text
                        print("\nERROR: incorrect param return %s"%r.text)
                        s += "\nERROR: incorrect param return %s"%r.text
                    elif not expected.issubset(j):
                        log["insufficient"][url] = method + "  "+r.text
                        print("\nERROR: insufficient params %s"%r.text)
                        s += "\nERROR: insufficient params %s"%r.text
                    else:
                        log["ok"][url] = method + "  "+r.text
                        print("\nSUCCESS %s"%r.text)
                        s += "\nSUCCESS %s"%r.text
                except json.JSONDecodeError:
                    log["json"][url] = "\nERROR: json decode error: "+ method + "  "+r.text
                    print("\nERROR: json decode: "+ r.text)
                    s += "\nERROR: json decode: "+ r.text
        except:
            log["timeout"][url] = method + "  "+"exception error"
            print("\nERROR: timeout, might be from icorrent URL")
            s += "\nERROR: timeout, might be from icorrent URL"
    return s, 200, {'Content-Type': 'text/plain; charset=utf-8'}


def save(reason):
        k = sorted(log[reason].keys())
        for x in log[reason]:
            print(x, json.dumps(log[reason][x]).replace('\\','')[:80])


@app.route('/')
def index():
    print("ok", flush=True)
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/check')
def info():
    print("ok", flush=True)
    url = request.args.get('url')
    print(url, flush=True)
    return main(url)

if __name__ == '__main__':
    print("starting", flush=True)
    app.run(host='0.0.0.0')
