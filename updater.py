import wget
from os import remove, getcwd, system, rename, rmdir, path, listdir
from pandas import *
import time
import zipfile


filepath = getcwd()+"\\Update\\"
updatingUpdater = False

##Fonction de verification de la version installée et de recherche de mises à jour
def trouverMAJ():
    ignoredFiles = ["PythonEnv","config.csv","tuteurs.csv","feedback.csv","relations.csv","lastestlog.txt","makePackage.py","PackageMakerLang",".git"]
    """Recherche de mise a jour pour le logiciel principal"""
    with open(file=str(filepath)+"version.txt",mode='r') as versionActuelle:
        versioninstallee = versionActuelle.read()
        versionActuelle.close()
    wget.download('https://jrucvl.github.io/CAPalgorythm/version.txt', str(filepath)+'server-version.txt')
    with open(file=str(filepath)+"server-version.txt", mode="r") as versionServer:
        derniereversion = versionServer.read()
        versionServer.close()
    print(derniereversion == versioninstallee)
    if derniereversion == versioninstallee:
        pass
    else:
        for e in listdir(getcwd()):
            if e == 'fr-Xabi08-CAPAlgorythmCore':
                for f in listdir('fr-Xabi08-CAPAlgorythmCore'):
                    if f != "__pycache__":
                        remove(path.join('fr-Xabi08-CAPAlgorythmCore', f))
                    else:
                        for g in listdir('fr-Xabi08-CAPAlgorythmCore/__pycache__'):
                            remove(path.join('fr-Xabi08-CAPAlgorythmCore/__pycache__', g))
                        rmdir('fr-Xabi08-CAPAlgorythmCore/__pycache__')
            elif e == 'Update':
                for f in listdir('Update'):
                    remove(path.join('Update', f))
                remove('Update')
            elif e in ignoredFiles:
                pass
            else:
                remove(e)
        try:
            rmdir(path = 'fr-Xabi08-CAPAlgorythmCore')
        except FileNotFoundError:
            pass
        wget.download("https://jrucvl.github.io/CAPalgorythm/software-version.zip",'software.zip')
        zipPath = str(getcwd())+"/software.zip"
        with zipfile.ZipFile(zipPath, 'r') as zip:
            zip.extractall(getcwd())
        system("PythonEnv/App/Python/python.exe -m pip install -r {0}/libs.txt")
        system("finishupdate.bat")
    print("\nCleaning up...")
    remove(path=str(filepath)+'server-version.txt')
    """Fin du programme de mise a jour """
    print("Update done.")
    quit()

trouverMAJ()
