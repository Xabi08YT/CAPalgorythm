import pandas
import os
from datetime import datetime
import unidecode


CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["basicDBCtrl"],0)


creneaux = {"LU0": "Lundi de 8h à 9h","LU1": "Lundi de 9h à 10h","LU2": "Lundi de 10h à 11h","LU3": "Lundi de 11h à 12h","LU4": "Lundi de 12h à 13h","LU5": "Lundi de 13h à 14h","LU6": "Lundi de 14h à 15h","LU7": "Lundi de 15h à 16h","LU8": "Lundi de 16h à 17h","LU9":"Lundi de 17h à 18h",
                "MA0": "Mardi de 8h à 9h","MA1": "Mardi de 9h à 10h","MA2": "Mardi de 10h à 11h","MA3": "Mardi de 11h à 12h","MA4": "Mardi de 12h à 13h","MA5": "Mardi de 13h à 14h","MA6": "Mardi de 14h à 15h","MA7": "Mardi de 15h à 16h","MA8": "Mardi de 16h à 17h","MA9":"Mardi de 17h à 18h",
                "ME0": "Mercredi de 8h à 9h","ME1": "Mercredi de 9h à 10h","ME2": "Mercredi de 10h à 11h","ME3": "Mercredi de 11h à 12h",
                "JE0": "Jeudi de 8h à 9h","JE1": "Jeudi de 9h à 10h","JE2": "Jeudi de 10h à 11h","JE3": "Jeudi de 11h à 12h","JE4": "Jeudi de 12h à 13h","JE5": "Jeudi de 13h à 14h","JE6": "Jeudi de 14h à 15h","JE7": "Jeudi de 15h à 16h","JE8": "Jeudi de 16h à 17h","JE9":"Jeudi de 17h à 18h",
                "VE0": "Vendredi de 8h à 9h","VE1": "Vendredi de 9h à 10h","VE2": "Vendredi de 10h à 11h","VE3": "Vendredi de 11h à 12h","VE4": "Vendredi de 12h à 13h","VE5": "Vendredi de 13h à 14h","VE6": "Vendredi de 14h à 15h","VE7": "Vendredi de 15h à 16h","VE8": "Vendredi de 16h à 17h","VE9":"Vendredi de 17h à 18h",}


newLogs = False
isDB1loaded = False
isDB2loaded = False
isDB3loaded = True
isConfigLoaded = False
relDB = None
feedback = None

##Fonction d'Ecriture d'informations de debuggage
def printInLogs(objet, categorie, forceshowing = False):
    if config["enableLogs"] == True or forceshowing == True:
        with open(file="lastestlog.txt", mode="a+") as logs:
            if categorie == 0:
                logs.writelines(str(datetime.now())+"/[INFO] : "+str(objet)+"\n")
            elif categorie == 1:
                logs.writelines(str(datetime.now())+"/[WARN] : "+str(objet)+"\n")
            elif categorie == 2:
                logs.writelines(str(datetime.now())+"/[ERR] : "+str(objet)+"\n")
            elif categorie == 3:
                logs.writelines(str(datetime.now())+"/[FATAL] : "+str(objet)+"\n")
            logs.close()
        return

#####################################################
#                   Init                            #
#####################################################

def init():
    global tuteursDB,relDB, feedback, config, isConfigLoaded, isDB1loaded, isDB2loaded, isDB3loaded, newLogs
    for i in range(2):
        if isConfigLoaded == False:
            config = {"enableLogs": True, "enableFeedback": False, "enableRelDB": False}
            if newLogs == False:
                try:
                    os.remove("lastestlog.txt")
                except FileNotFoundError:
                    pass
                newLogs = True
            printInLogs("Début de l'initialisation du programme...", 0)
            printInLogs("Chargement de la configuration...",0)
            for i in range(3):
                try:
                    try:
                        cfg = pandas.read_csv("config.csv")
                        printInLogs("Configuration chargée. Construction et application de la configuration lue...", 0)
                        config["enableLogs"] = cfg.loc[0,"state"]
                        config["enableFeedback"] = cfg.loc[1,"state"]
                        config["enableRelDB"] = cfg.loc[2,"state"]
                        printInLogs("Table de configuration Construite et Appliquée.", 0, True)
                        break
                    except FileNotFoundError:
                        CoreLibs.basicDBCtrl.createDB("config.csv",["properties","state"], [{"properties": "enableLogs", "state": True},{"properties": "enableFeedback", "state": False},{"properties": "enableRelDB", "state": False}])
                        printInLogs("Impossible de charger la configuration à cause d'un fichier inexistant. Création d'une configuration vierge...", 1)
                except KeyError:
                    printInLogs("Impossible d'appliquer la configuration. Utilisation de la configuration par défaut...", 2)
                    break
            if i==3:
                printInLogs("Impossible de charger la configuration. Utilisation de la configuration par défaut...", 2)
            isConfigLoaded = True
        printInLogs("Chargement des fichiers en cours...", 0)
        for i in range(3):
            if not(isDB1loaded):
                try:
                    tuteursDB = pandas.read_csv("tuteurs.csv")
                    printInLogs("La Base de Données tuteurs.csv à été chargée avec succès.", 0)
                    isDB1loaded = True
                except FileNotFoundError:
                    CoreLibs.basicDBCtrl.createDB("tuteurs.csv", fieldnames = ['nom', 'prenom','niveau','disponibilites','matiere','contact'])
                    printInLogs("Impossible de charger la Base de Données tuteurs.csv vu que le fichier est introuvable. Ce fichier à été ajouté au répertoire courant.", 1)
            if not(isDB2loaded) and config["enableRelDB"]:
                try:
                    relDB = pandas.read_csv("relations.csv")
                    printInLogs("La Base de Données relations.csv à été chargée avec succès.", 0)
                    isDB2loaded = True
                except FileNotFoundError:                    
                    CoreLibs.basicDBCtrl.createDB("relations.csv", fieldnames = ["id","tuteur","tutore","matiere","horaire"])
                    printInLogs("Impossible de charger la Base de Données relations.csv vu que le fichier est introuvable. Ce fichier à été ajouté au répertoire courant.", 1)
            """if not(isDB3loaded):
                try:
                    feedback = pandas.read_csv("feedback.csv")
                    printInLogs("La Base de Données feedback.csv à été chargée avec succès.", 0)
                    isDB3loaded = True
                except FileNotFoundError:
                    with open(file="feedback.csv", mode="a+",newline="") as temp:
                        tempw = csv.DictWriter(temp, fieldnames = ["prenomtutore","nomtutore","prenomtuteur","nomtuteur","avistutore","avistuteur","typeavis"])
                        tempw.writeheader()
                        temp.close()"""
            if isDB1loaded and isDB2loaded and isDB3loaded:
                break
        if i == 3:
            printInLogs("Initialisation s'est terminée à cause d'une erreur: Echec du chargement des fichiers. Le programme va maintenant s'arrêter.", 3)
            quit()
        printInLogs("Chargement des fichiers terminé.",0)
        printInLogs("Initialisation du programme terminée avec succès. Démarrage...",0)
        break
    return


def getVars():
    return (tuteursDB,relDB, feedback, config, isConfigLoaded, isDB1loaded, isDB2loaded, isDB3loaded, newLogs)


def unloadDB():
    global isDB1loaded, isDB2loaded, isDB3loaded
    isDB1loaded = False
    isDB2loaded = False
    return


def actualiserDB():
    global tuteursDB, relDB, feedback
    try:
        tuteursDB = pandas.read_csv("tuteurs.csv")
        relDB = pandas.read_csv("relations.csv")
        feedback = pandas.read_csv("feedback.csv")
    except FileNotFoundError:
        global isDB1loaded, isDB2loaded, isDB3loaded
        isDB1loaded = False
        isDB2loaded = False
        init()
    return tuteursDB, relDB, feedback


def actualiserConfig():
    global config
    printInLogs("Actualisation de la configuration...",0, True)
    try:
        cfg = pandas.read_csv("config.csv")
        printInLogs("Configuration chargée. Construction et application de la configuration lue...", 0)
        config["enableLogs"] = cfg.loc[0,"state"]
        config["enableFeedback"] = cfg.loc[1,"state"]
        config["RelDB"] = cfg.loc[2,"state"]
        printInLogs("Table de configuration Construite et Appliquée.", 0, True)
    except FileNotFoundError:
        CoreLibs.basicDBCtrl.createDB("config.csv",["properties","state"], [{"properties": "enableLogs", "state": True},{"properties": "enableFeedback", "state": False},{"properties": "RelDB", "state": False}])
        printInLogs("Impossible de charger la configuration à cause d'un fichier inexistant. Création d'une configuration vierge...", 1)
    return config


def unicode_serialize(texts):
    for i in range(len(texts)):
        print(texts[i])
        string_sortie = unidecode.unidecode(texts[i])
        print(string_sortie)
        texts[i] = string_sortie
    return texts