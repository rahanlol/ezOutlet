import requests
import time

t = float(input("Please enter desired period:  "))
length = int(
    input("Please enter desired ammount of time to run this script (in s): "))

n = int(length / t)

print(f"{n} times")

IP = "10.167.111.153"
USER = "admin"
PASSWD = "0D7BDA"
URL = f"http://{IP}/cgi-bin/control2.cgi"

for i in range(n):
    r = requests.get(URL, params={
        "user":   USER,
        "passwd": PASSWD,
        "target": 1,
        "control": 2  # 2 for power alternate
    }, timeout=5)
    r.raise_for_status()
    print(f"[{i}] HTTP {r.status_code} → {r.text.strip()}")
    time.sleep(t)  # duration of sleep time
