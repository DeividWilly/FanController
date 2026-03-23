import requests
import json
import time
import wmi
import os
import pathlib

url = str("http://localhost:8085/data.json")
cRPM = 20
path = str(r"")


class FanController:
    def __init__(self, alpha=0.1):
        self.rpm = 50
        self.alpha = alpha

    def getTemp(api_url):
        response = requests.get(api_url)
    
        if response.status_code == 200:
            data = response.json()
            actualTemp = int(data["Children"][0]["Children"][1]["Children"][3]["Children"][10]["Value"].replace(".0 °C", ""))
        
            return actualTemp

        else:
            print(f"ERROR: {response.status_code}")

    def getCpuLoad(api_url):
        response = request.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            cpuLoad = float(data["Children"][0]["Children"][1]["Children"][4]["Children"][0]["Value"].replace(" %", ""))
            
            return cpuLoad
        else:
            print(f"ERROR: {response.status_code}")
            
    def setRPM(actualTemp):
        if actualTemp <= 50:
            targetRPM = 20
        
        elif actualTemp <= 60:
            targetRPM = 30
        
        elif actualTemp <= 70:
            targetRPM = 50
            
        elif actualTemp <= 80:
            targetRPM = 70
                
        elif actualTemp <= 120:
            targetRPM = 100
        
        return targetRPM
        
    def smoothRPM(target):
        sRPM = target
        sRPM = int((0.5 * target) + (1 - 0.5) * sRPM)
        return sRPM
        
def verifyApp():
    f = wmi.WMI()
    
    flag = 0
    
    for process in f.Win32_Process():
        if "LibreHardwareMonitor.exe" == process.Name:
            flag = 1
            return True
    if flag == 0:
        return False
        
def getRAM():
    f = wmi.WMI()
    
    for memory in f.Win32_PerfFormattedData_PerfOS_Memory():
        RAM = memory.PercentCommittedBytesInUse
        return RAM

if verifyApp() == False:
    os.startfile(path)
    time.sleep(15)
    
while True:
    try:
        temp = FanController.getTemp(url)
        tRPM = FanController.setRPM(temp)
        cRPM = int((0.5 * tRPM) + ((1 - 0.5) * cRPM))
        #cRPM = FanController.smoothRPM(tRPM)
        print(f"\rTemp: {temp} | Target RPM: {cRPM}%", end='')
        time.sleep(1)
    except KeyboardInterrupt:
        break