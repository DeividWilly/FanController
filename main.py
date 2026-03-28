import requests
import json
import time
import wmi
import os
import pathlib


folder = ['Aga.Controls.dll', 'Aga.Controls.pdb', 'BlackSharp.Core.dll', 'de', 'DiskInfoToolkit.dll', 'es', 'fr', 'HidSharp.dll', 'it', 'ja', 'LibreHardwareMonitor.config', 'LibreHardwareMonitor.exe', 'LibreHardwareMonitor.exe.config', 'LibreHardwareMonitorLib.dll', 'LibreHardwareMonitorLib.pdb', 'LibreHardwareMonitorLib.xml', 'Microsoft.Bcl.AsyncInterfaces.dll', 'Microsoft.Bcl.HashCode.dll', 'Microsoft.Win32.TaskScheduler.dll', 'OxyPlot.dll', 'OxyPlot.WindowsForms.dll', 'pl', 'RAMSPDToolkit-NDD.dll', 'README.md', 'ru', 'sv', 'System.Buffers.dll', 'System.CodeDom.dll', 'System.Collections.Immutable.dll', 'System.Formats.Nrbf.dll', 'System.IO.Pipelines.dll', 'System.Memory.dll', 'System.Numerics.Vectors.dll', 'System.Reflection.Metadata.dll', 'System.Resources.Extensions.dll', 'System.Runtime.CompilerServices.Unsafe.dll', 'System.Security.AccessControl.dll', 'System.Security.Principal.Windows.dll', 'System.Text.Encodings.Web.dll', 'System.Text.Json.dll', 'System.Threading.AccessControl.dll', 'System.Threading.Tasks.Extensions.dll', 'tr', 'zh-CN', 'zh-Hant']

port = "8085"
url = str(f"http://localhost:{port}/data.json")
path = str(r"LibreHardwareMonitor\LibreHardwareMonitor.exe")

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
            return self.temp, self.lastTemp
            
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

sensor = CPU()
print(sensor.getTemp(url))
print(sensor.getLoad(url))