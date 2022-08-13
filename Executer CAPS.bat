@echo off
echo launching updater...
PythonEnv\App\Python\python.exe updater.py
echo   OK !
echo launching...
PythonEnv\App\Python\python.exe main.py
pause