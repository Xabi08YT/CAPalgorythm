from os import getcwd, rename
from zipfile import ZipFile
from PackageMakerLang import FR


APP_PATH = getcwd()
language = "EN"

modules = {1: None, 2: FR.init(), 3: None}

def langSelect():
    print("Deployment package  making program")
    print("Please select your language")
    print("1: EN")
    print("2: FR")
    print("3: DE")
    print("E: Exit")
    try:
        choice = input()
        if choice.upper() == "E":
            quit()
        else:
            choice = int(choice)
    except ValueError as e:
        quit(e)


langSelect()