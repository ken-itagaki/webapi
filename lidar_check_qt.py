import requests

params = ["action=get&object=ethernet_all",
          "action=get&object=lidar_config",
          "action=get&object=device_info",
          "action=get&object=lidar_sync",
          "action=get&object=lidar_data&key=lidar_range",
          "action=get&object=lidar_data&key=lidar_mode",
          "action=get&object=lidar_data&key=standbymode",]

ip = "192.168.120.211"

for param in params:
    repo_url = f"http://{ip}/pandar.cgi?{param}"
    response = requests.get(repo_url)
    print(response.text)