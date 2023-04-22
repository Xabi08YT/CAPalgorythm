from os import system, getcwd, path, listdir, remove
from shutil import copy
from zipfile import ZipFile


ignoredElementsUpdate= ["config.csv","tuteurs.csv","relations.csv","lastestlog.txt","LICENSE","readme.md","feedbakc.csv","PythonEnv","PakageMakerLang",".gitignore","makePackage.py","updater.py"]


def createInstallPackage():
    print("Choose the platform:")
    print("1: Windows 7 and greater")
    print("2: Windows 10 and greater")
    print("3: MacOS (UNSUPPORTED YET)")
    print("4: Linux (UNSUPPORTED YET)")
    print("5: All of the above")
    try:
        choice = int(input())
        if choice == 1:
            pass
        elif choice==2:
            pass
        else:
            print("UNSUPPORTED, returning to main menu...")
            return
    except Exception:
        print("ERR: invalid. Returning to main menu...")
        return


def createUpdatePackage():
    try:
        remove('newupdater.py')
        remove('software-version.zip')
    except FileNotFoundError:
        pass
    try:
        copy("updater.py","newupdater.py")
        zipDir = getcwd()+'/software-version.zip'
        with ZipFile(zipDir, "x") as pkg:
            for e in listdir(getcwd()):
                if e in ignoredElementsUpdate:
                    pass 
                else:
                    pkg.write(path.join(getcwd(),e))
            pkg.close()
        remove("newupdater.py")
        print("Success. Update package is now ready to be deployed.")
        choice = input("Do You wish to return to main menu? (y/n): ")
        if choice.lower() == "y":
            return
        else:
            quit()
    except FileNotFoundError:
        print("ERR: Missing files to create an update. Aborting...")


def menu():
    while 1:
        print("Menu: \n 1: Create install package")
        print("2: Create update package")
        print("3: Exit")
        try:
            choice = int(input())
            if choice == 3:
                break
            elif choice == 2:
                createUpdatePackage()
            elif choice == 1:
                createInstallPackage()
        except ValueError:
            print("ERR: Invalid. Please retry.")
    return

menu()