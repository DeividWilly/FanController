import sys
import time
import wmi
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
           
if __name__ == "__main__": 
    if verifyApp() == True:
        print("\n" * 3)

        pc = PC()
        s = Controller()

        while True:
            
            time.sleep(1)
    else:
        print("erro")