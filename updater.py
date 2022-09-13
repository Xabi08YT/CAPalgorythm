import wget
from os import remove, getcwd, system, rename
from pandas import *

filepath = getcwd()+"\\Update\\"

##Fonction de verification de la version installée et de recherche de mises à jour
def trouverMAJ():
    print("Checking for software update....")
    """Recherche de mise a jour pour le logiciel principal"""
    with open(file=str(filepath)+"version.txt",mode='r') as versionActuelle:
        versioninstallee = versionActuelle.read()
        wget.download('https://jrucvl.github.io/CAPalgorythm/version.txt', str(filepath)+'server-version.txt')
        with open(file=str(filepath)+"version.txt", mode="r") as versionServer:
            derniereversion = versionServer.read()
            if derniereversion == versioninstallee:
                pass
            else:
                remove(path = 'main.py')
                wget.download("https://jrucvl.github.io/CAPalgorythm/main.py",'main.py')
                with open(file=str(filepath)+'version.txt', mode = "w") as version:
                    version.writelines(derniereversion)
                    version.close()
                    remove("logo.png")
                wget.download("https://jrucvl.github.io/CAPalgorythm/logo.png", 'logo.png')
    print("\nChecking for libraries update....")
    """Recherche de mises a jour pour les programmes auxiliaires..."""
    with open(file = str(filepath)+"libs.txt", mode = 'r') as liblist:
        liblistlocal = liblist.readlines()
        wget.download('https://jrucvl.github.io/CAPalgorythm/libs.txt', str(filepath)+'server-libs.txt')
        with open(file = str(filepath)+'server-libs.txt', mode = 'r') as serverliblist:
            serverlibs = serverliblist.readlines()
            if liblistlocal == serverlibs:
                pass
            else:
                with open(file = 'updatelibs.txt', mode = 'a+') as updatecommand:
                    for i in range(len(serverlibs)):
                        updatecommand.writelines("/PythonEnv/App/Python/Scripts/pip.exe install "+str(servlibs[i]))
                    updatecommand.close()
                rename("updatelibs.txt", "updatelibs.bat")
                system("updatecommand.bat")
                with open(file = str(filepath)+'libs.txt', mode = 'w') as libversion:
                    libversion.writelines(serverlibs)
                    libversion.close()
            serverliblist.close()
        liblist.close()
    print("\nChecking updater version....")
    """Recherche de mises a jour du programme de mise a jour..."""
    with open(file = str(filepath)+"updaterversion.txt", mode = 'r') as localupdaterver:
        uversion = localupdaterver.readline()
        wget.download("https://jrucvl.github.io/CAPalgorythm/updaterversion.txt", str(filepath)+"updaterserverversion.txt")
        with open(file = str(filepath)+"updaterserverversion.txt", mode = 'r') as serverupdaterver:
            serveruversion = serverupdaterver.readline()
            if serveruversion == uversion:
                pass
            else:
                with open(file = 'finishupdate.txt', mode = 'a+') as command:
                    command.writelines("@echo off\n")
                    command.writelines("echo The program need to be restarted to complete the update. Please wait...\n")
                    command.writelines("timeout /t 1\n")
                    command.writelines("del updater.py")
                    command.writelines("rename newupdater.py, updater.py\n")
                    command.writelines("start 'Executer CAPS.bat\n")
                    command.writelines("del finishupdate.bat")
                    command.close()
                with open(file = str(filepath)+"updaterversion.txt", mode = 'w') as uver:
                    uver.writelines(serveruversion)
                    uver.close()
                wget.download("https://jrucvl.github.io/CAPalgorythm/updater.py", "newupdater.py")
                serverupdaterver.close()
                rename('finishupdate.txt','finishupdate.bat')
            localupdaterver.close()
    print("\nCleaning up....")
    """Suppression des fichiers temporaires necessaires aux mises a jour"""
    remove(path = str(filepath)+'server-libs.txt')
    try:
        remove(path = "updatecommand.bat")
    except FileNotFoundError:
        pass
    remove(path=str(filepath)+'server-version.txt')
    remove(path=str(filepath)+'updaterserverversion.txt')
    if updatingUpdater:
        system("finishupdate.bat")
    """Fin du programme de mise a jour """
    print("Update done.")
    quit()
trouverMAJ()
