import requests
import time


n = int(input("Please enter desired ammount of loops: "))
t = float(input("Please enter desired period:  "))

IP = "10.167.111.153"
USER = "admin"
PASSWD = "0D7BDA"
URL = f"http://{IP}/cgi-bin/control2.cgi"

for i in range(n):
    r = requests.get(URL, params={
        "user":   USER,
        "passwd": PASSWD,
        "target": 1,
        "control": 2  # 2 for power off, 1 for power on
    }, timeout=5)
    r.raise_for_status()
    print(f"[{i}] HTTP {r.status_code} → {r.text.strip()}")
    time.sleep(t)  # duration of sleep time
