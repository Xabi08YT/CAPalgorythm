IF exist  "PythonEnv" call install.bat
pythonvenv\Scripts\python.exe updater.py
pythonvenv\Scripts\python.exe main.py
pause