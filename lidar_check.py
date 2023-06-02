import requests

ip_list = ["192.168.110.201",
           "192.168.110.202",
           "192.168.110.204",
           "192.168.120.203",
           "192.168.120.211",
           "192.168.120.212",
           "192.168.120.213",
           "192.168.120.214"]

params = ["action=get&object=ethernet_all",
          "action=get&object=lidar_config",
          "action=get&object=device_info",
          "action=get&object=lidar_sync",
          "action=get&object=lidar_data&key=lidar_range",
          "action=get&object=lidar_data&key=lidar_mode",
          "action=get&object=lidar_data&key=standbymode"]

mask = "255.255.255.0"
gateway = ["192.168.110.1","192.168.120.1"]
spinspeed = "2"
destip = "255.255.255.255"
destport = ["2321","2322","2324","2323","2331","2332","2333","2334"]
clocksource = "1"
domain = "0"
logannounceinterval = "1"
logsyncinterval = "1"
logmindelayreqinterval = "0"
network = "0"
angle_setting_methods = 0
lidar_range1 = 900
lidar_range2 = 2700
lidar_range3 = 3750
lidar_range4 = 30
syncAngle = ["180","270","0","270","180","270","90","0"]

def ethernet_all(response,ip):
    lidar_setting=response.json()["Body"]["Control_IP"]["IPv4"]
    if lidar_setting != ip:
        print(ip,"IPaddress is wrong")
    lidar_setting=response.json()["Body"]["Control_IP"]["Mask"]
    if lidar_setting != mask:
        print(ip,"IPmask is wrong")
    lidar_setting=response.json()["Body"]["Control_IP"]["Gateway"]
    if ip == "192.168.110.201"or ip=="192.168.110.202"or ip=="192.168.110.204":
        if lidar_setting != gateway[0]:
            print(ip,"IPGateway is wrong")
    elif ip == "192.168.120.203"or ip=="192.168.120.211"or ip=="192.168.120.212"or\
               ip=="192.168.120.213"or ip=="192.168.120.214":
        if lidar_setting != gateway[1]:
            print(ip,"IPGateway is wrong")
            
def lidar_config(response,ip):
    if ip == "192.168.110.201"or ip=="192.168.110.202"or ip=="192.168.110.204":
        lidar_setting=response.json()["Body"]["SpinSpeed"]
        if lidar_setting != spinspeed:
            print(ip,"SpinSpeed is wrong")
    lidar_setting=response.json()["Body"]["DestIp"]
    if lidar_setting != destip:
        print(ip,"DestIp is wrong")
    lidar_setting=response.json()["Body"]["DestPort"]
    if ip == "192.168.110.201":
        if lidar_setting != destport[0]:
            print(ip,"DestPort is wrong")
    elif ip == "192.168.110.202":
        if lidar_setting != destport[1]:
            print(ip,"DestPort is wrong")
    elif ip == "192.168.110.204":
        if lidar_setting != destport[2]:
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.203":
        if lidar_setting != destport[3]:
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.211":
        if lidar_setting != destport[4]:
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.212":
        if lidar_setting != destport[5]:
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.213":
        if lidar_setting != destport[6]:
            print(ip,"DestPort is wrong")
    elif ip == "192.168.120.214":
        if lidar_setting != destport[7]:
            print(ip,"DestPort is wrong")
    lidar_setting=response.json()["Body"]["ClockSource"]
    if lidar_setting != clocksource:
            print(ip,"ClockSource is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting[10]
    if ptpconfig != domain:
        print(ip,"Domain is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting[46]
    if ptpconfig != logannounceinterval:
        print(ip,"LogAnnounceInterval is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting[66]
    if ptpconfig != logsyncinterval:
        print(ip,"LogSyncInterval is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting[93]
    if ptpconfig != logmindelayreqinterval:
        print(ip,"LogMinDelayReqInterval is wrong")
    if ip == "192.168.110.201"or ip=="192.168.110.202"or ip=="192.168.110.204":
        lidar_setting=response.json()["Body"]["NoiseFiltering"]
        if lidar_setting != "1":
            print(ip,"NoiseFiltering is wrong")
        lidar_setting=response.json()["Body"]["ReflectivityMapping"]
        if lidar_setting != "0":
            print(ip,"ReflectivityMapping is wrong")
    lidar_setting=response.json()["Body"]["PTPProfile"]
    if lidar_setting != "0":
        print(ip,"PTPProfile is wrong")
    lidar_setting=response.json()["Body"]["PTPConfig"]
    ptpconfig = lidar_setting[22]
    if ptpconfig != network:
        print(ip,"Networks is wrong")
    if ip == "192.168.120.211"or ip=="192.168.120.212"or\
            ip=="192.168.120.213"or ip=="192.168.120.214":
        lidar_setting=response.json()["Body"]["RotateDirection"]
        if lidar_setting != "0":
            print(ip,"RotateDirection is wrong")
    

def lidar_sync(response,ip):
    lidar_setting=response.json()["Body"]["syncAngle"]
    if ip == ip_list[0]:
        if lidar_setting != syncAngle[0]:
            print(ip,"syncAngle is wrong")
    elif ip == ip_list[1]:
        if lidar_setting != syncAngle[1]:
            print(ip,"syncAngle is wrong")
    elif ip == ip_list[2]:
        if lidar_setting != syncAngle[2]:
            print(ip,"syncAngle is wrong")
    elif ip == ip_list[3]:
        if lidar_setting != syncAngle[3]:
            print(ip,"syncAngle is wrong")
    elif ip == ip_list[4]:
        if lidar_setting != syncAngle[4]:
            print(ip,"syncAngle is wrong")
    elif ip == ip_list[5]:
        if lidar_setting != syncAngle[5]:
            print(ip,"syncAngle is wrong")
    elif ip == ip_list[6]:
        if lidar_setting != syncAngle[6]:
            print(ip,"syncAngle is wrong")
    elif ip == ip_list[7]:
        if lidar_setting != syncAngle[7]:
            print(ip,"syncAngle is wrong")

def lidar_range(response,ip):
    lidar_setting=response.json()["Body"]["angle_setting_method"]
    if lidar_setting != angle_setting_methods:
        print(ip,"angle_setting_methods is wrong")
    if ip == ip_list[3]:
        lidar_setting=response.json()["Body"]["lidar_range"]
        if lidar_setting[0] != lidar_range4:
            print(ip,"lidar_range is wrong")
        if lidar_setting[1] != lidar_range2:
            print(ip, "lidar_range is wrong")
    elif ip == ip_list[1]:
        lidar_setting=response.json()["Body"]["lidar_range"]
        if lidar_setting[0] != lidar_range1:
            print(ip,"lidar_range is wrong")
        if lidar_setting[1] != lidar_range3:
            print(ip, "lidar_range is wrong")
    else:
        lidar_setting=response.json()["Body"]["lidar_range"]
        if lidar_setting[0] != lidar_range1:
            print(ip,"lidar_range is wrong")
        if lidar_setting[1] != lidar_range2:
            print(ip, "lidar_range is wrong")

def lidar_mode(response,ip):
    if ip == "192.168.110.201"or ip=="192.168.110.202"or ip=="192.168.110.204"or ip=="192.168.120.203":
        lidar_setting=response.json()["Body"]["lidar_mode"]
        if lidar_setting != "2":
            print(ip,"lidar_mode is wrong")
    elif ip == "192.168.120.211"or ip=="192.168.120.212"or\
            ip=="192.168.120.213"or ip=="192.168.120.214":
        lidar_setting=response.json()["Body"]["lidar_mode"]
        if lidar_setting != "3":
            print(ip,"lidar_mode is wrong")
def stanbymode(response,ip):
    lidar_setting=response.json()["Body"]["standbymode"]
    if lidar_setting != "0":
        print(ip,"standbymodess is wrong")

def device_info(response,ip):
    if ip=="192.168.110.201"or ip=="192.168.110.202"or ip=="192.168.110.204"or ip=="192.168.120.203":
        lidar_setting=response.json()["Body"]["Udp_Seq"]
        if lidar_setting != "0":
            print(ip,"Udp_Seq is wrong")
    lidar_setting=response.json()["Body"]["Trigger_Method"]
    if lidar_setting != "0":
        print(ip,"Trigger_Method is wrong")

def main():
    for ip in ip_list:
        for param in params:
            try:
                repo_url = f"http://{ip}/pandar.cgi?{param}"
                response = requests.get(repo_url)
                if param == params[0]:
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
            except:
                pass

if __name__ == '__main__':
    main()







