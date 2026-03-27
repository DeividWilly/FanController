import requests
import json
import time
import wmi
import os
import pathlib
from download import port

folder = ['Aga.Controls.dll', 'Aga.Controls.pdb', 'BlackSharp.Core.dll', 'de', 'DiskInfoToolkit.dll', 'es', 'fr', 'HidSharp.dll', 'it', 'ja', 'LibreHardwareMonitor.config', 'LibreHardwareMonitor.exe', 'LibreHardwareMonitor.exe.config', 'LibreHardwareMonitorLib.dll', 'LibreHardwareMonitorLib.pdb', 'LibreHardwareMonitorLib.xml', 'Microsoft.Bcl.AsyncInterfaces.dll', 'Microsoft.Bcl.HashCode.dll', 'Microsoft.Win32.TaskScheduler.dll', 'OxyPlot.dll', 'OxyPlot.WindowsForms.dll', 'pl', 'RAMSPDToolkit-NDD.dll', 'README.md', 'ru', 'sv', 'System.Buffers.dll', 'System.CodeDom.dll', 'System.Collections.Immutable.dll', 'System.Formats.Nrbf.dll', 'System.IO.Pipelines.dll', 'System.Memory.dll', 'System.Numerics.Vectors.dll', 'System.Reflection.Metadata.dll', 'System.Resources.Extensions.dll', 'System.Runtime.CompilerServices.Unsafe.dll', 'System.Security.AccessControl.dll', 'System.Security.Principal.Windows.dll', 'System.Text.Encodings.Web.dll', 'System.Text.Json.dll', 'System.Threading.AccessControl.dll', 'System.Threading.Tasks.Extensions.dll', 'tr', 'zh-CN', 'zh-Hant']

port = "8085"
url = str(f"http://localhost:{port}/data.json")
cRPM = 20
path = str(r"LibreHardwareMonitor\LibreHardwareMonitor.exe")

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