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

