import network
import time
import urequests

SERVER_IP = "192.168.1.63"

def read_wifi_config(filename):
    '''Reads wifi config file'''
    with open(filename, 'rt') as f:
        s = f.readlines()
    return s[0].strip(), s[1].strip()


class THLData():
    def __init__(self, location, time, T, RH, LUX):
        self.location = location
        self.time = time
        self.T = T
        self.RH = RH
        self.LUX = LUX
                    
    def __str__(self):
        return "{" + f'''"location":'{self.location}',"timestamp":{self.time},"T":{self.T},"RH":{self.RH},"LUX":{self.LUX}''' + "}"
    
    
def wifi_connect(config_file):    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    username, password = read_wifi_config(config_file)
    wlan.connect(username, password)
    
    while not wlan.isconnected() and wlan.status() >= 0:
        print("waiting to connect:")
        time.sleep(1)
    print(wlan.ifconfig())


def run():
    wifi_connect('wifi.txt')

    thl_data = THLData(
            "livingroom",
            time.localtime(),
            23.5,
            50.5,
            34
        )


    try:
        r = urequests.request("GET","http://192.168.1.63:8080/tasks/rp2040/")
        pr = urequests.request("POST","http://192.168.1.63:8080/tasks/rp2040/", data=str(thl_data))
    except OSError:
        print("Failed to Connect to the Server.")
    else:
        print(r.status_code)
        if r.status_code == 200:
            print(r.content)
            r.close()
            
        if pr.status_code == 200:
            print(pr.content)
            pr.close()

if __name__ == "__main__":
    print("main")
    run()