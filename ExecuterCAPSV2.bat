IF exist "ExecuterCAPS.bat" del "ExecuterCAPS.bat"
IF exist "PythonEnv" .\PythonEnv\App\Python\python.exe migration.py 
IF exist "PythonEnv" rmdir PythonEnv /s /q
IF exist "migration.py" del "migration.py"
pythonvenv\Scripts\python.exe updater.py
pythonvenv\Scripts\python.exe main.py
pause