import xml.etree.ElementTree as ET
# <add key="runWebServerMenuItem" value="true" />

def configXML(configPath, port):
    
    tree = ET.parse(configPath)
    root = tree.getroot()
    
    for elem in root.findall(".//add"):
        if elem.get("key") == "runWebServerMenuItem":
            elem.set("value", "true")
            print("WebServer activated.")
            
        elif elem.get("key") == "listenerPort":
            elem.set("value", port)
            print(f"WebServer port set to {port}")
            
    tree.write(configPath, encoding="utf-8", xml_declaration=True)
    print(f"File saved in {configPath} Please restart the LibreHardwareMonitor process manually.")
    
configXML("LibreHardwareMonitor/LibreHardwareMonitor.config", "8086")