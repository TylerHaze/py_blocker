from datetime import datetime as dt
import time

# hosts_path = r"C:\Windows\System32\drivers\etc\hosts" this is the real path which requires admin permissions
hosts_path = r"C:\Users\Tyler\Documents\hosts.txt"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", "www.reddit.com", "reddit.com"]

todayam = dt.now().replace(hour=9, minute=00, second=0, microsecond=0)
todaypm = dt.now().replace(hour=17, minute=0, second=0, microsecond=0)

while True:
    now = dt.now()
    if todayam <= now <= todaypm:
        with open(hosts_path, 'r+') as hostFile:
            content = hostFile.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    hostFile.write(redirect+" "+website+"\n")
    else:
        with open(hosts_path,'+r') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)        
            file.truncate() 
        time.sleep(5)
