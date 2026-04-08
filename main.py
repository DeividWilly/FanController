import sys
import time
import wmi
import json
from Controller import Controller
from PC import PC

port = "8085"
url = str(f"http://localhost:{port}/data.json")
path = str(r"LibreHardwareMonitor\LibreHardwareMonitor.exe")

def build(cpuTemperature, cpuLoad, totalRAM, usedRAM, rpm):
    return json.dumps(
        {"t": cpuTemperature, "l": cpuLoad, "tr": totalRAM, "ur": usedRAM, "r": rpm}, separators=(',', ':')
        )

def verifyApp():
    pc = wmi.WMI()
    
    for process in pc.Win32_Process():
        if "LibreHardwareMonitor.exe" == process.Name:
            return True
    return False
           
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
            uram = round(pc.getRAM()[2], 1)
            tram = round(pc.getRAM()[0], 1)
            
            data = build(temp, load, tram, uram, srpm)
            
            time.sleep(1)
    else:
        print("erro")