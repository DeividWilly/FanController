import pathlib
import zipfile
from urllib.request import urlretrieve

version_app = "v0.9.6"
package_link = f"https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/{version_app}/LibreHardwareMonitor.zip"
filename = "LibreHardwareMonitor.zip"

# Download do arquivo - ok
# Extração do arquivo - ok
# Modificação do xml para ativar o web server - em progresso <add key="runWebServerMenuItem" value="true" />

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
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall("LibreHardwareMonitor")

check = checkFile(filename)
if check == True:
    print("Arquivo já existe")
else:
    print("Arquivo não existe, providenciando download...")
    downloadFile(package_link, filename)
    extractFile(filename)