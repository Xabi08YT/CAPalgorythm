import os
from datetime import datetime
import unidecode
import sqlite3


CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["DBCreator","cfgHandler"],0)


creneaux = {"LU0": "Lundi de 8h à 9h","LU1": "Lundi de 9h à 10h","LU2": "Lundi de 10h à 11h","LU3": "Lundi de 11h à 12h","LU4": "Lundi de 12h à 13h","LU5": "Lundi de 13h à 14h","LU6": "Lundi de 14h à 15h","LU7": "Lundi de 15h à 16h","LU8": "Lundi de 16h à 17h","LU9":"Lundi de 17h à 18h",
                "MA0": "Mardi de 8h à 9h","MA1": "Mardi de 9h à 10h","MA2": "Mardi de 10h à 11h","MA3": "Mardi de 11h à 12h","MA4": "Mardi de 12h à 13h","MA5": "Mardi de 13h à 14h","MA6": "Mardi de 14h à 15h","MA7": "Mardi de 15h à 16h","MA8": "Mardi de 16h à 17h","MA9":"Mardi de 17h à 18h",
                "ME0": "Mercredi de 8h à 9h","ME1": "Mercredi de 9h à 10h","ME2": "Mercredi de 10h à 11h","ME3": "Mercredi de 11h à 12h",
                "JE0": "Jeudi de 8h à 9h","JE1": "Jeudi de 9h à 10h","JE2": "Jeudi de 10h à 11h","JE3": "Jeudi de 11h à 12h","JE4": "Jeudi de 12h à 13h","JE5": "Jeudi de 13h à 14h","JE6": "Jeudi de 14h à 15h","JE7": "Jeudi de 15h à 16h","JE8": "Jeudi de 16h à 17h","JE9":"Jeudi de 17h à 18h",
                "VE0": "Vendredi de 8h à 9h","VE1": "Vendredi de 9h à 10h","VE2": "Vendredi de 10h à 11h","VE3": "Vendredi de 11h à 12h","VE4": "Vendredi de 12h à 13h","VE5": "Vendredi de 13h à 14h","VE6": "Vendredi de 14h à 15h","VE7": "Vendredi de 15h à 16h","VE8": "Vendredi de 16h à 17h","VE9":"Vendredi de 17h à 18h",}


newLogs = False
isConfigLoaded = False

##Fonction d'Ecriture d'informations de debuggage
def printInLogs(objet, categorie, forceshowing = False):
    if config["enableLogs"] == True or forceshowing == True:
        with open(file="latestlog.txt", mode="a+") as logs:
            if categorie == 0:
                logs.writelines(str(datetime.now())+"/[INFO] : "+str(objet)+"\n")
            elif categorie == 1:
                logs.writelines(str(datetime.now())+"/[WARN] : "+str(objet)+"\n")
            elif categorie == 2:
                logs.writelines(str(datetime.now())+"/[ERR] : "+str(objet)+"\n")
            elif categorie == 3:
                logs.writelines(str(datetime.now())+"/[FATAL] : "+str(objet)+"\n")
            elif categorie == 4:
                logs.writelines(str(datetime.now())+"/[CONSOLEOUT] : "+str(objet)+"\n")
            logs.close()
        return


def transformToText(strlist):
    out = ""
    for e in strlist:
        out += e
    return out


#####################################################
#                   Init                            #
#####################################################

def init():
    global config
    config = CoreLibs.cfgHandler.getCfg()
    printInLogs("Configuration chargée et appliquée.",0)
    try:
        os.remove("latestlog.txt")
    except FileNotFoundError:
        pass
    printInLogs("Chargement des fichiers en cours...", 0)
    for i in range(3):
        try:
            global MainDB
            MainDB = sqlite3.connect("data.db")
            break
        except FileNotFoundError:
            try:
                CoreLibs.DBCreator.createDB()
            except Exception as e:
                printInLogs('Erreur lors de la création de la base de données : ' + str(e),3)
                exit(-1)
        except Exception as e:
            printInLogs('Erreur lors du chargement de la base de données : ' + str(e),3)
            exit(-1)
    if i == 3:
        printInLogs("Initialisation s'est terminée à cause d'une erreur: Echec du chargement des fichiers. Le programme va maintenant s'arrêter.", 3)
        quit()
    printInLogs("Chargement des fichiers terminé.",0)
    printInLogs("Initialisation du programme terminée avec succès. Démarrage...",0)
    return


def getVars():
    return (MainDB, config, isConfigLoaded, newLogs)


def unloadDB():
    MainDB.close()
    return


def actualiserDB():
    global MainDB
    MainDB.close()
    try:
        MainDB = sqlite3.connect("data.db")
    except FileNotFoundError:
        CoreLibs.DBCreator.createDB()
    return MainDB


def actualiserConfig():
    global config
    config = CoreLibs.cfgHandler.getCfg()
    printInLogs("Configuration actualisée.",0)
    return config


def unicode_serialize(text):
    for i in range(len(text)):
        strOut = unidecode.unidecode(text[i])
        text[i] = strOut
    return text