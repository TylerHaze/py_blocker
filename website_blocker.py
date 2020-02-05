from datetime import datetime as dt
import time

# hosts_path = r"C:\Windows\System32\drivers\etc\hosts" this is the real path which requires admin permissions
hosts_path = r"C:\Users\Tyler\Documents\hosts.txt"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.reddit.com", "reddit.com"]

while True:
    now = dt.now()
    today8am = now.replace(hour=7, minute=0, second=0, microsecond=0)
    if now >= today8am:
        with open(hosts_path, 'a') as hostFile:
            hostFile.write("")
        time.sleep(300)
    else:
        print("not yet")
        time.sleep(5)
