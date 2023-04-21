from os import system, getcwd, path, listdir
from zipfile import ZipFile


ignoredElementsUpdate= ["config.csv","tuteurs.csv","relations.csv","ExecuterCAPS.bat","lastestlog.txt","LICENSE","readme.md","feedbakc.csv","PythonEnv","PakageMakerLang",".gitignore","makePackage.py"]


def createInstallPackage():
    print("Choisissez la plateforme:")
    print("1: Windows 7 et plus")
    print("2: Windows 10 et plus")
    print("3: MacOS (Non supporté pour le moment)")
    print("4: Linux (Non supporté pour le moment)")
    try:
        choice = int(input())
        if choice == 1:
            pass
        elif choice==2:
            pass
        else:
            print("Fonctionnalité non implémentée/supportée, retour au menu principal.")
            return
    except Exception:
        print("Choix invalide. Retour au menu principal.")
        return


def createUpdatePackage():
    system('cp updater.py newupdater.py')
    zipDir = getcwd()+'/server-software.zip'
    with ZipFile(zipDir, "a+") as pkg:
        for e in listdir(getcwd()):
            if e in ignoredElementsUpdate:
                pass 
            else:
                pkg.write(path.join(getcwd,e))


modeChoice = {1: createInstallPackage, 2: createUpdatePackage, 3: quit}

def menu():
    while 1:
        print("Menu: \n 1: Créer un package d'installation")
        print("2: Créer un package de Mise à Jour")
        print("3: Quitter")
        try:
            choice = int(input())
            modeChoice[choice]
            return
        except ValueError or KeyError:
            print("Choix invalide. Rééssayez svp")
    return


def init():
    while 1:
        menu()

