import os
from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/ngome/Downloads/Router3_running-config.txt") #/ "Router3_running-config.txt"

ruta_windows = PureWindowsPath("C:/Users/ngome/Downloads/Router3_running-config.txt")
#MI_ARCHIVO = open(carpeta)

print(ruta_windows)