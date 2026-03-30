import requests
import json
import time
import wmi
import os
import pathlib

port = "8085"
url = str(f"http://localhost:{port}/data.json")
path = str(r"LibreHardwareMonitor\LibreHardwareMonitor.exe")


class PC():
    def __init__(self):
        self.ramUsed = 0
        self.ramFree = 0
        self.gpuLoad = 0
        self.vramUsed = 0
        self.vramFree = 0
        self.gpuLoad = 0
        self.gpuTemp = 0
        self.cpuLoad = 0
        self.cpuTemp = 0

class CPU():
    def __init__(self):
        self.temp = 0
        self.lastTemp = 0
        self.load = 0.1
    
    def getTemp(self, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            self.temp = int(data["Children"][0]["Children"][1]["Children"][3]["Children"][10]["Value"].replace(".0 °C", ""))
            return self.temp
            
        else:
            print("ERROR")
            return None
            
    def getLoad(self, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            self.load = float(data["Children"][0]["Children"][1]["Children"][4]["Children"][0]["Value"].replace(" %", ""))
            return self.load
        else:
            print("ERROR")
            return None
            
class Controller():
    def __init__(self):
        self.rpmCurve = [
        (50, 20),
        (60, 40),
        (70, 60),
        (80, 80),
        (120, 100)]
        
        self.tempLimit = 3
        self.alpha_up = 0.7
        self.alpha_down = 0.2
        self.lastRPM = None
        

    def setRPM(self, cpuTemperature):
        for temp, rpm in self.rpmCurve:
            if cpuTemperature <= temp:
                return rpm
        return 100

    def smoothRPM(self, targetRPM):
        if self.lastRPM is None:
            self.lastRPM = float(targetRPM)
            return targetRPM

        if abs(targetRPM - self.lastRPM) < 2:
            return int(self.lastRPM)

        if targetRPM > self.lastRPM:
            alpha = self.alpha_up
        else:
            alpha = self.alpha_down

        smoothed = (
            alpha * targetRPM + (1 - alpha) * self.lastRPM
        )

        self.lastRPM = smoothed
        return int(smoothed)
        
def verifyApp():
    pc = wmi.WMI()
    
    for process in pc.Win32_Process():
        if "LibreHardwareMonitor.exe" == process.Name:
            return True
    return False
            
sensor = CPU()
control = Controller()

if verifyApp() == False:
    print("LibreHardwareMonitor not running, starting...")
    os.startfile(path)
    time.sleep(20)
    
while True:
    temp = sensor.getTemp(url)
    rpm = control.setRPM(temp)
    srpm = control.smoothRPM(rpm)

    print(f"\rcpu temp: {temp} | cpu load: {None} | rpm target: {rpm}% | rpm smoothed: {srpm}%", end="")
    time.sleep(1)