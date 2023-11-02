from shutil import rmtree
from os import system


def install():
    system(".\PythonEnv\App\Python\python.exe -m venv pythonvenv")
    system(".\pythonvenv\Scripts\python.exe -m pip install -r Update/libs.txt")

install()