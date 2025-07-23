import requests
import time

i = 1
IP = "10.167.111.153"
USER = "admin"
PASSWD = "0D7BDA"
URL = f"http://{IP}/cgi-bin/control2.cgi"

r = requests.get(URL, params={
    "user":   USER,
    "passwd": PASSWD,
    "target": 1,
    "control": 0
}, timeout=5)

while True:
    inputON = str(input("Press ENTER to turn ON (q to quit): "))
    if inputON.lower() == "q":
        break
    else:
        r = requests.get(URL, params={
            "user":   USER,
            "passwd": PASSWD,
            "target": 1,
            "control": 1
        }, timeout=5)
        r.raise_for_status()
        print(f"[{i}] HTTP {r.status_code} → {r.text.strip()}")
        i += 1
        inputOFF = str(input("Press ENTER to turn OFF (q to quit): "))
        if inputOFF.lower() == "q":
            break
        else:
            r = requests.get(URL, params={
                "user":   USER,
                "passwd": PASSWD,
                "target": 1,
                "control": 0
            }, timeout=5)
        r.raise_for_status()
        print(f"[{i}] HTTP {r.status_code} → {r.text.strip()}")
        i += 1
        continue
