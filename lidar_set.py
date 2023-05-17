import requests

ip_list = ["192.168.110.201",
           "192.168.110.202",
           "192,168,110.204"]

params =["action=set&object=lidar&key=spin_speed&value=2"]

for ip in ip_list:
    for param in params:
        try:
            repo_url = f"http://{ip}/pandar.cgi?{param}"
            response = requests.get(repo_url)
        except:
             pass