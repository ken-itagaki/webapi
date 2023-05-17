import requests
import json

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
    lidar_setting=response.json()["Body"]["Control_IP"]["IPv4"]
    print(ip,"IPaddress is",lidar_setting)
    lidar_setting=response.json()["Body"]["Control_IP"]["Mask"]
    print(ip,"IPmask is",lidar_setting)
    lidar_setting=response.json()["Body"]["Control_IP"]["Gateway"]
    print(ip,"IPGateway is",lidar_setting)
            
def lidar_config(response,ip):
    lidar_setting=response.json()["Body"]["SpinSpeed"]
    print(ip,"SpinSpeed",lidar_setting)
    lidar_setting=response.json()["Body"]["DestIp"]
    print(ip,"DestIp is",lidar_setting)
    lidar_setting=response.json()["Body"]["DestPort"]
    print(ip,"DestPort is",lidar_setting)
    lidar_setting=response.json()["Body"]["ClockSource"]
    print(ip,"ClockSource is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["PTPConfig"]["Domain"])
    print(ip,"Domain is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["PTPConfig"]["LogAnnounceInterval"])
    print(ip,"LogAnnounceInterval is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["PTPConfig"]["LogSyncInterval"])
    print(ip,"LogSyncInterval is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["PTPConfig"]["LogMinDelayReqIntervals"])
    print(ip,"LogMinDelayReqInterval is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["NoiseFiltering"])
    print(ip,"NoiseFiltering is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["ReflectivityMapping"])
    print(ip,"ReflectivityMapping is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["PTPProfile"])
    print(ip,"PTPProfile is",lidar_setting)
    ptpconfig = json.loads(response.text)
    lidar_setting=json.loads(ptpconfig["Body"]["Networks"])
    print(ip,"Networks is",lidar_setting)

def lidar_sync(response,ip):
    lidar_setting=response.json()["Body"]["syncAngle"]
    print(ip,"syncAngle is",lidar_setting)

def lidar_range(response,ip):
    lidar_setting=response.json()["Body"]["angle_setting_method"]
    print(ip,"angle_setting_methods is",lidar_setting)
    lidar_setting=response.json()["Body"]["lidar_range"]
    print(ip,"lidar_range is",lidar_setting[0])
    print(ip, "lidar_range is",lidar_setting[1])

def lidar_mode(response,ip):
    lidar_setting=response.json()["Body"]["lidar_mode"]
    print(ip,"lidar_mode is",lidar_setting)
    
def stanbymode(response,ip):
    lidar_setting=response.json()["Body"]["standbymode"]
    print(ip,"standbymodess is",lidar_setting)

def device_info(response,ip):
    lidar_setting=response.json()["Body"]["Udp_Seq"]
    print(ip,"Udp_Seq is",lidar_setting)
    lidar_setting=response.json()["Body"]["Trigger_Method"]
    print(ip,"Trigger_Method is",lidar_setting)

def code_range(response,ip):
    lidar_setting=response.json()
    print(lidar_setting)
     

count = 0

for ip in ip_list:
    for param in params:
        try:
            repo_url = f"http://{ip}/pandar.cgi?{param}"
            response = requests.get(repo_url)
            if param == params[0]:
                print(param)
                ethernet_all(response,ip)
            elif param == params[1]:
                print(param)
                lidar_config(response,ip)
            elif param == params[2]:
                print(param)
                device_info(response,ip)
            elif param ==params[3]:
                 print(param)
                 lidar_sync(response,ip)
            elif param == params[4]:
                print(param)
                lidar_range(response,ip)
            elif param == params[5]:
                print(param)
                lidar_mode(response,ip)
            elif param == params[6]:
                print(param)
                stanbymode(response,ip)
            elif param == params[7]:
                print(param)
                code_range(response,ip)
        except:
             pass







