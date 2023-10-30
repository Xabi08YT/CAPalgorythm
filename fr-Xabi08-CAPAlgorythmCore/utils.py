import os
from datetime import datetime
import unidecode
import sqlite3
import sys


class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)


old_stdout = sys.stdout


CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["DBCreator","cfgHandler"],0)


creneaux = {"LU0": "Lundi de 8h à 9h","LU1": "Lundi de 9h à 10h","LU2": "Lundi de 10h à 11h","LU3": "Lundi de 11h à 12h","LU4": "Lundi de 12h à 13h","LU5": "Lundi de 13h à 14h","LU6": "Lundi de 14h à 15h","LU7": "Lundi de 15h à 16h","LU8": "Lundi de 16h à 17h","LU9":"Lundi de 17h à 18h",
                "MA0": "Mardi de 8h à 9h","MA1": "Mardi de 9h à 10h","MA2": "Mardi de 10h à 11h","MA3": "Mardi de 11h à 12h","MA4": "Mardi de 12h à 13h","MA5": "Mardi de 13h à 14h","MA6": "Mardi de 14h à 15h","MA7": "Mardi de 15h à 16h","MA8": "Mardi de 16h à 17h","MA9":"Mardi de 17h à 18h",
                "ME0": "Mercredi de 8h à 9h","ME1": "Mercredi de 9h à 10h","ME2": "Mercredi de 10h à 11h","ME3": "Mercredi de 11h à 12h",
                "JE0": "Jeudi de 8h à 9h","JE1": "Jeudi de 9h à 10h","JE2": "Jeudi de 10h à 11h","JE3": "Jeudi de 11h à 12h","JE4": "Jeudi de 12h à 13h","JE5": "Jeudi de 13h à 14h","JE6": "Jeudi de 14h à 15h","JE7": "Jeudi de 15h à 16h","JE8": "Jeudi de 16h à 17h","JE9":"Jeudi de 17h à 18h",
                "VE0": "Vendredi de 8h à 9h","VE1": "Vendredi de 9h à 10h","VE2": "Vendredi de 10h à 11h","VE3": "Vendredi de 11h à 12h","VE4": "Vendredi de 12h à 13h","VE5": "Vendredi de 13h à 14h","VE6": "Vendredi de 14h à 15h","VE7": "Vendredi de 15h à 16h","VE8": "Vendredi de 16h à 17h","VE9":"Vendredi de 17h à 18h",}

matieres = ['Allemand', 'Anglais', 'Education Morale et Civique', 'Enseignement scientifique Physique', 'Enseignement-scientifique SVT', 'Espagnol', 'Francais', 'HGGSP', 'HLP', 'Histoire-Geographie', 'Litt. Anglaise', 'Mathematiques', 'Mathematiques tronc-commun (TC)', 'Musique', 'NSI/SNT', 'Philosophie', 'Physique Spe', 'SES', 'SVT Spe']


def transformToText(strlist):
    out = ""
    for e in strlist:
        out += e
    return out


#####################################################
#                   Init                            #
#####################################################

def init():
    global config, log_file
    config = CoreLibs.cfgHandler.getCfg()
    log_file = open("latest.log","w")
    sys.stdout = Unbuffered(log_file)
    print("Configuration chargée et appliquée.",0)
    try:
        os.remove("latestlog.txt")
    except FileNotFoundError:
        pass
    print("Chargement des fichiers en cours...", 0)
    for i in range(3):
        if "data.db" in os.listdir():
            global MainDB
            MainDB = sqlite3.connect("data.db", check_same_thread=False)
            break
        else:
            try:
                CoreLibs.DBCreator.createDB(config["enableRel"],config["enableFeedback"])
            except Exception as e:
                print('Erreur lors de la création de la base de données : ' + str(e),3)
                exit(-1)
    if i == 3:
        print("Initialisation s'est terminée à cause d'une erreur: Echec du chargement des fichiers. Le programme va maintenant s'arrêter.", 3)
        quit()
    print("Chargement des fichiers terminé.",0)
    print("Initialisation du programme terminée avec succès. Démarrage...",0)
    return


def getVars():
    return (config, MainDB)


def unloadDB():
    MainDB.close()
    return


def refreshDB():
    global MainDB
    MainDB.close()
    try:
        MainDB = sqlite3.connect("data.db", check_same_thread=False,)
    except FileNotFoundError:
        CoreLibs.DBCreator.createDB()
    return MainDB


def refreshConfig():
    global config
    config = CoreLibs.cfgHandler.getCfg()
    return config


def unicode_serialize(text):
    for i in range(len(text)):
        strOut = unidecode.unidecode(text[i])
        text[i] = strOut.lower()
    return text


def parseSubjects(input,forGetRequest = False):
    input = input.split(",")
    if not forGetRequest:
        finalTXT = ""
        for i,e in enumerate(input):
            if e.lower() == "true":
                finalTXT += matieres[i]
        return finalTXT
    lengths = 0
    finalTXT = []
    for i,e in enumerate(input):
        if e.lower() == "true":
            finalTXT += ["_"*lengths+matieres[i]+"%"]
        lengths += len(matieres[i])
    return finalTXT


def parseDispos(input,forGetRequest = False):
    input = input.split(",")
    if not forGetRequest:
        finalTXT = ""
        for i,e in enumerate(input):
            if e.lower() == "true":
                finalTXT += list(creneaux.keys())[i]
        return finalTXT
    lengths = 0
    finalTXT = []
    for i,e in enumerate(input):
        if e.lower() == "true":
            finalTXT += ["_"*lengths+list(creneaux.keys())[i]+"%"]
        lengths += len(list(creneaux.keys())[i])
    return finalTXT


def stop():
    sys.stdout = old_stdout
    log_file.close()
    return


def createModifyRequest(input):
    input = input.decode('utf-8')
    eid = input.split("+")[1][0]
    input = input.replace("+"+eid,"")
    input = input.split("&")
    updateRq = "UPDATE '"+input[0].split("=")[1]+"' SET "
    for e in input:
        if not("table=" in e or ("id=" in e and not "groupid=" in e)):
            updateRq+=e.split("=")[0]+"='"+e.split("=")[1]+"',"
    updateRq = updateRq[:-1]
    updateRq+=" WHERE "+input[1]
    return updateRq


def resetDB():
    global MainDB
    MainDB.close()
    os.remove("data.db")
    CoreLibs.DBCreator.createDB(config["enableRel"],config["enableFeedback"])
    MainDB = sqlite3.connect("data.db", check_same_thread=False)
    return