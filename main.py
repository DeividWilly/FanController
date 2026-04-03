import requests
import json
import time
import wmi
import os
import pathlib

port = "8085"
url = str(f"http://localhost:{port}/data.json")
path = str(r"LibreHardwareMonitor\LibreHardwareMonitor.exe")

def verifyApp():
    pc = wmi.WMI()
    
    for process in pc.Win32_Process():
        if "LibreHardwareMonitor.exe" == process.Name:
            return True
    return False
            
# sensor = CPU()
# control = Controller()

# if verifyApp() == False:
    # print("LibreHardwareMonitor not running, starting...")
    # os.startfile(path)
    # time.sleep(20)
    
# while True:
    # temp = sensor.getTemp(url)
    # rpm = control.setRPM(temp)
    # srpm = control.smoothRPM(rpm)

    # print(f"\rcpu temp: {temp} | cpu load: {None} | rpm target: {rpm}% | rpm smoothed: {srpm}%", end="")
    # time.sleep(1)


while True:
    pc = PC()
    print(f"\r{pc.getRAM()[2]:.1f}/{pc.getRAM()[0]:.1f} GB", end="")
    time.sleep(0.7)