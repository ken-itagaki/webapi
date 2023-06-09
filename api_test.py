import requests

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
          "action=get&object=lidar_data&key=code_range&security_code=921223",
          "action=get&object=lidar_data&key=security_code_status"]

def ethernet_all(response,ip):
    lidar_setting=response.json()["Body"]["IPv4"]
    if lidar_setting != ip:
        print(ip,"IPaddress is wrong")
    lidar_setting=response.json()["Body"]["Mask"]
    if lidar_setting != "255.255.255.0":
        print(ip,"IPmask is wrong")
    lidar_setting=response.json()["Body"]["Gateway"]
    if ip == "192.168.110.201"or"192.168.110.202"or"192.168.110.204":
        if lidar_setting != "192.168.110.1":
            print(ip,"IPGateway is wrong")
    elif ip == "192.168.120.203"or"192.168.120.211"or"192.168.120.212"or\
               "192.168.120.213"or"192.168.120.214":
        if lidar_setting != "192.168.120.1":
            print(ip,"IPGateway is wrong")
            
def lidar_config(response,ip):
    lidar_setting=response.json()["Body"]["SpinSpeed"]
    if lidar_setting != "2":
        print(ip,"SpinSpeed is wrong")
    lidar_setting=response.json()["Body"]["DestIp"]
    if lidar_setting != "255.255.255.255":
        print(ip,"DestIp is wrong")
    lidar_setting=response.json()["Body"]["DestPort"]
    if ip == "192.168.110.201":
        if lidar_setting != "2321":
            print(ip,"DestPort is wrong")
    elif ip == "192.168.110.202":
        if lidar_setting != "2322":
            print(ip,"DestPort is wrong")
    elif ip == "192.168.110.204":
        if lidar_setting != "2324":
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.203":
        if lidar_setting != "2323":
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.211":
        if lidar_setting != "2331":
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.212":
        if lidar_setting != "2332":
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.213":
        if lidar_setting != "2333":
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.214":
        if lidar_setting != "2334":
            print(ip,"DestPort is wrong")
    lidar_setting=response.json()["Body"]["ClockSource"]
    if lidar_setting != "1":
            print(ip,"ClockSource is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting["Domain"]
    if ptpconfig != "0":
        print(ip,"Domain is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting["LogAnnounceInterval"]
    if ptpconfig != "1":
        print(ip,"LogAnnounceInterval is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting["LogSyncInterval"]
    if ptpconfig != "1":
        print(ip,"LogSyncInterval is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting["LogMinDelayReqInterval"]
    if ptpconfig != "0":
        print(ip,"LogMinDelayReqInterval is wrong")
    lidar_setting=response.json()["Body"]["NoiseFiltering"]
    if lidar_setting != "1":
            print(ip,"NoiseFiltering is wrong")
    lidar_setting=response.json()["Body"]["ReflectivityMapping"]
    if lidar_setting != "0":
            print(ip,"ReflectivityMapping is wrong")
    lidar_setting=response.json()["Body"]["PTPProfile"]
    if lidar_setting != "0":
            print(ip,"PTPProfile is wrong")
    lidar_setting=response.json()["Body"]["Network"]
    if lidar_setting != "0":
            print(ip,"Networks is wrong")

def lidar_sync(response,ip):
    lidar_setting=response.json()["Body"]["syncAngle"]
    if lidar_setting != "180":
            print(ip,"syncAngle is wrong")

def lidar_range(response,ip):
    lidar_setting=response.json()["Body"]["angle_setting_method"]
    if lidar_setting != "0":
            print(ip,"angle_setting_methods is wrong")
    lidar_setting=response.json()["Body"]["lidar_range"]
    print(lidar_setting)
    #if lidar_setting != "180":
     #       print(ip,"lidar_range is wrong")

def lidar_mode(response,ip):
    lidar_setting=response.json()["Body"]["lidar_mode"]
    if lidar_setting != "2":
        print(ip,"lidar_mode is wrong")
    
def stanbymode(response,ip):
    lidar_setting=response.json()["Body"]["standbymode"]
    if lidar_setting != "0":
        print(ip,"standbymodess is wrong")

def device_info(response,ip):
    lidar_setting=response.json()["Body"]["Udp_Seq"]
    if lidar_setting != "0":
        print(ip,"Udp_Seq is wrong")
    lidar_setting=response.json()["Body"]["Trigger_Method"]
    if lidar_setting != "0":
        print(ip,"Trigger_Method is wrong")

def code_range(response,ip):
    lidar_setting=response.json()
    print(lidar_setting)
    #if lidar_setting != "0":
    #    print(ip,"Trigger_Method is wrong")
     

count = 0

for ip in ip_list:
    for param in params:
        try:
            repo_url = f"http://{ip}/pandar.cgi?{param}"
            response = requests.get(repo_url)
            ethernet_all(response,ip_list[count])
            lidar_config(response,ip_list[count])
            lidar_sync(response,ip_list[count])
            lidar_range(response,ip_list[count])
            lidar_mode(response,ip_list[count])
            stanbymode(response,ip_list[count])
            device_info(response,ip_list[count])
            code_range(response,ip_list[count])
        except:
             pass
    count += 1
    print(count)







