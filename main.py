import sys
import time
import wmi
import json
from Controller import Controller
from PC import PC

port = "8085"
url = str(f"http://localhost:{port}/data.json")
path = str(r"LibreHardwareMonitor\LibreHardwareMonitor.exe")

def verifyApp():
    pc = wmi.WMI()
    
    for process in pc.Win32_Process():
        if "LibreHardwareMonitor.exe" == process.Name:
            return True
    return False

def buildJson(cpuTemp, cpuLoad, fanRPM, ramUsage, totalRAM):
        dict = {
                "c": cpuTemp,
                "cl": cpuLoad,
                "r": fanRPM,
                "ru": round(ramUsage, 1), 
                "tr": round(totalRAM, 1)
                }
        data = json.dumps(dict)
        return data
        
if __name__ == "__main__": 
    if verifyApp() == True:
        print("\n" * 3)

        pc = PC()
        s = Controller()

        while True:
            temp = pc.getTemp(url)
            load = pc.getLoad(url)
            rpm = s.setRPM(temp)
            srpm = s.smoothRPM(rpm)
            uram = pc.getRAM()[2]
            tram = pc.getRAM()[0]
            
            a = buildJson(temp, load, srpm, uram, tram)
            print(a)
            time.sleep(1)
    else:
        print("erro")