import pathlib
import zipfile
import sys
import xml.etree.ElementTree as ET
from urllib.request import urlretrieve

version_app = "v0.9.6"
package_link = f"https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/{version_app}/LibreHardwareMonitor.zip"
filename = "LibreHardwareMonitor.zip"
port = "8085"

def checkFile(path):
    f = pathlib.Path(path)
    if f.exists():
        return True
    else:
        return False

def downloadFile(url, fileName):
    print(f"Downloading LibreHardwareMonitor {version_app} from GitHub...")
    urlretrieve(url, fileName)
    print("Done!")
    
def extractFile(file):
    print("Descompactando...")
    try:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall("LibreHardwareMonitor")
    except PermissionError:
        f = pathlib.Path(file)
        f.unlink()
        print("File running. Please close the LibreHardwareMonitor process and try again.")
        sys.exit(1)
        
def configXML(configPath, port):
    
    tree = ET.parse(configPath)
    root = tree.getroot()
    
    for elem in root.findall(".//add"):
        if elem.get("key") == "runWebServerMenuItem": # <add key="runWebServerMenuItem" value="true" />
            elem.set("value", "true")
            print("WebServer activated.")
            
        elif elem.get("key") == "listenerPort": # <add key="listenerPort" value="8085" />
            elem.set("value", port)
            print(f"WebServer port set to {port}")
            
    tree.write(configPath, encoding="utf-8", xml_declaration=True)
    print(f"File saved in {configPath}")
    print("Manually restart the LibreHardwareMonitor process if it is already running to ensure the configuration is correct.")

check = checkFile(filename)

if check == True:
    print("File has exists.")
    
else:
    print("Downloading...")
    downloadFile(package_link, filename)
    extractFile(filename)
    configXML("LibreHardwareMonitor/LibreHardwareMonitor.config", port)