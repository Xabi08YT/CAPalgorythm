rmdir PythonEnv /s /q
python -m venv pythonvenv
cd Update
pythonvenv\Scripts\python.exe -m pip install -r libs.txt
cd ../
pause
pythonvenv\Scripts\python.exe main.py