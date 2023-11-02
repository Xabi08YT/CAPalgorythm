IF exist  "PythonEnv" install.bat
cd Update
..\pythonvenv\Scripts\python.exe -m pip install -r libs.txt
cd ..\
pythonvenv\Scripts\python.exe main.py
pause