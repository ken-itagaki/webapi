import requests
import json
import time

ip_list = ["192.168.110.201",
           "192.168.110.202",
           "192,168,110.204"]

params = ["action=get&object=ethernet_all",
          "action=get&object=lidar_config",
          "action=get&object=device_info",
          "action=get&object=lidar_sync",
          "action=get&object=lidar_data&key=lidar_range",
          "action=get&object=lidar_data&key=lidar_mode",
          "action=get&object=lidar_data&key=standbymode",
          "action=get&object=lidar_data&key=code_range&security_code=921223"]

def ethernet_all(response,ip):
    lidar_setting=response.json()
    a = lidar_setting.get("Body", {}).get("Control_IP", {})
    ipv4 = a.get("IPv4")
    print(ipv4)
    if ipv4 == ip:
        print(ip,"IPaddress is ok")
    mask = a.get("Mask")
    if mask == "255.255.255.0":
        print(ip,"IPmask is ok")
    gateway = a.get("Gateway")
    if ip == "192.168.110.201"or"192.168.110.202"or"192.168.110.204":
        if gateway == "192.168.110.1":
            print(ip,"IPGateway is ok")
    elif ip == "192.168.120.203"or"192.168.120.211"or"192.168.120.212"or\
               "192.168.120.213"or"192.168.120.214":
        if gateway == "192.168.120.1":
            print(ip,"IPGateway is ok")
            
def lidar_config(response,ip):
    lidar_setting=response.json()["Body"]["SpinSpeed"]
    if lidar_setting == "2":
        print(ip,"SpinSpeed is ok")
    lidar_setting=response.json()["Body"]["DestIp"]
    if lidar_setting == "255.255.255.255":
        print(ip,"DestIp is ok")
    lidar_setting=response.json()["Body"]["DestPort"]
    if ip == "192.168.110.201":
        if lidar_setting == "2321":
            print(ip,"DestPort is ok")
    elif ip == "192.168.110.202":
        if lidar_setting == "2322":
            print(ip,"DestPort is ok")
    elif ip == "192.168.110.204":
        if lidar_setting == "2324":
            print(ip,"DestPort is ok")
    elif ip == "192.168.120.203":
        if lidar_setting == "2323":
            print(ip,"DestPort is ok")
    elif ip == "192.168.120.211":
        if lidar_setting == "2331":
            print(ip,"DestPort is ok")
    elif ip == "192.168.120.212":
        if lidar_setting == "2332":
            print(ip,"DestPort is ok")
    elif ip == "192.168.120.213":
        if lidar_setting == "2333":
            print(ip,"DestPort is ok")
    elif ip == "192.168.120.214":
        if lidar_setting == "2334":
            print(ip,"DestPort is ok")
    lidar_setting=response.json()["Body"]["ClockSource"]
    if lidar_setting == "1":
        print(ip,"ClockSource is ok")
    lidar_setting=json.loads(response.text)
    ptpconfig = json.loads(lidar_setting['Body']['PTPConfig'])['Domain']
    print(ptpconfig)
    if ptpconfig == count:
        print(ip,"Domain is ok")
    lidar_setting=json.loads(response.text)
    ptpconfig = json.loads(lidar_setting['Body']['PTPConfig'])['LogAnnounceInterval']
    print(ptpconfig)
    if ptpconfig == "1":
        print(ip,"LogAnnounceInterval is ok")
    lidar_setting=json.loads(response.text)
    ptpconfig = json.loads(lidar_setting['Body']['PTPConfig'])['LogSyncInterval']
    print(ptpconfig)
    if ptpconfig == "1":
        print(ip,"LogSyncInterval is ok")
    lidar_setting=json.loads(response.text)
    ptpconfig = json.loads(lidar_setting['Body']['PTPConfig'])['LogMinDelayReqInterval']
    print(ptpconfig)
    if ptpconfig == "0":
        print(ip,"LogMinDelayReqInterval is ok")
    lidar_setting=response.json()
    a = lidar_setting.get("Body", {}).get("NoiseFiltering", {})
    ipv4 = a.get("IPv4")
    print(ipv4)
    lidar_setting=response.json()["Body"]["NoiseFiltering"]
    if lidar_setting == "1":
        print(ip,"NoiseFiltering is ok")
    lidar_setting=response.json()["Body"]["ReflectivityMapping"]
    if lidar_setting == "0":
        print(ip,"ReflectivityMapping is ok")
    lidar_setting=response.json()["Body"]["PTPProfile"]
    if lidar_setting == "0":
        print(ip,"PTPProfile is ok")
    lidar_setting=response.json()["Body"]["Network"]
    if lidar_setting == "0":
        print(ip,"Networks is ok")

def lidar_sync(response,ip):
    lidar_setting=response.json()["Body"]["syncAngle"]
    if lidar_setting == "180":
        print(ip,"syncAngle is ok")

def lidar_range(response,ip):
    lidar_setting=response.json()["Body"]["angle_setting_method"]
    print(lidar_setting)
    if lidar_setting == "0":
        print(ip,"angle_setting_methods is ok")
    lidar_setting=response.json()["Body"]["lidar_range"]
    print(lidar_setting[1])
    if lidar_setting[0] == "900":
        print(ip,"lidar_range is ok")
    if lidar_setting[1] == "2700":
        print(ip,"lidar_range is ok")

def lidar_mode(response,ip):
    lidar_setting=response.json()["Body"]["lidar_mode"]
    if lidar_setting == "2":
        print(ip,"lidar_mode is ok")
    
def stanbymode(response,ip):
    lidar_setting=response.json()["Body"]["standbymode"]
    if lidar_setting == "0":
        print(ip,"standbymodess is ok")

def device_info(response,ip):
    lidar_setting=response.json()["Body"]["Udp_Seq"]
    if lidar_setting == "0":
        print(ip,"Udp_Seq is ok")
    lidar_setting=response.json()["Body"]["Trigger_Method"]
    if lidar_setting == "0":
        print(ip,"Trigger_Method is ok")

def code_range(response,ip):
    lidar_setting=response.json()
    print(lidar_setting,"code_range")
    #if lidar_setting == "0":
    #    print(ip,"code is ok")
     

count = 0

for ip in ip_list:
    for param in params:
        try:
            repo_url = f"http://{ip}/pandar.cgi?{param}"
            time.sleep(1)
            response = requests.get(repo_url)
            if param == params[0]:
                print("eth")
                ethernet_all(response,ip)
            elif param == params[1]:
                lidar_config(response,ip)
            elif param == params[2]:
                device_info(response,ip)
            elif param ==params[3]:
                 lidar_sync(response,ip)
            elif param == params[4]:
                lidar_range(response,ip)
            elif param == params[5]:
                lidar_mode(response,ip)
            elif param == params[6]:
                stanbymode(response,ip)
            elif param == params[7]:
                code_range(response,ip)
        except:
             pass
    count += 1
    print(count)







