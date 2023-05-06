import wget
from os import remove, getcwd, system, rename, rmdir, path, listdir
import zipfile


filepath = getcwd()+"\\Update\\"
updatingUpdater = False

##Fonction de verification de la version installée et de recherche de mises à jour
def trouverMAJ():
    ignoredFiles = ["PythonEnv","config.csv","tuteurs.csv","feedback.csv","relations.csv","lastestlog.txt","makePackage.py","PackageMakerLang",".git", "ExecuterCAPS.bat"]
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
            if e == 'fr-Xabi08-CAPAlgorythmCore' or e == 'Update':
                for f in listdir(e):
                    if f != "__pycache__":
                        remove(path.join(e, f))
                    else:
                        for g in listdir(path.join(e, f)):
                            remove(path.join(e,f, g))
                        rmdir(path.join(e, f))
                rmdir(e)
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
        system("PythonEnv\App\Python\python.exe -m pip install -r \"{0}\"".format(path.join(str(getcwd()),"Update/libs.txt")))
        rename(src="newupdater.py",dst="updater.py")
    print("\nCleaning up...")
    remove("software.zip")
    """Fin du programme de mise a jour """
    print("Update done.")
    quit()

trouverMAJ()
