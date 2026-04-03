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
            temp = pc.getTemp(url)
            load = pc.getLoad(url)
            rpm = s.setRPM(temp)
            srpm = s.smoothRPM(rpm)
            uram = pc.getRAM()[2]
            tram = pc.getRAM()[0]
            
            sys.stdout.write("\033[3F")
            
            sys.stdout.write(f"Temp: {temp}°C\n")
            sys.stdout.write(f"CPU Load: {load}%\n")
            sys.stdout.write(f"RPM: {rpm}% -> {srpm}%\n")
            sys.stdout.write(f"RAM: {uram:.1f}/{tram:.1f}")
            sys.stdout.flush()
            
            time.sleep(1)
    else:
        print("erro")