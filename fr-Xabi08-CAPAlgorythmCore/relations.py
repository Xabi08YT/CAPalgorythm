import pandas
import csv
from random import randint
from os import remove
CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)


idList = []
IDLEN = 8


def addRel(infos):
    idToUse = generateID()
    row = {"id": idToUse, "tuteur": infos["tuteur"],"tutore": infos["tutore"],"matiere": infos["matiere"],"horaire": infos["horaire"]}
    with open(file = "relations.csv", mode = 'a+',newline="") as database:
        windb = csv.DictWriter(database, ["id","tuteur","tutore","matiere","horaire"])
        windb.writerow(row)
        database.close()
    return


def rmRel(id):
    DB = CoreLibs.utils.relDB
    index = None
    for i, row in DB.iterrows():
        if id == row["id"]:
            index = i
    _rels = DB.copy()
    print(index)
    remove("relations.csv")
    with open(file="relations.csv", mode="a+",newline="") as temp:
        tempw = csv.DictWriter(temp, fieldnames = ["id","tuteur","tutore","matiere","horaire"])
        tempw.writeheader()
        for j in range(len(_rels)):
            if j != index:
                tempw.writerow({"id": str(_rels.loc[j,"id"]).strip(), "tuteur":str(_rels.loc[j,"tuteur"]),"tutore": str(_rels.loc[j,"tutore"]).strip(), "matiere": str(_rels.loc[j,"matiere"]).strip(), "horaire": str(_rels.loc[j,"horaire"]).strip()})
        temp.close()
    return


def checkRels(nom, prenom, matiere):
    DB = CoreLibs.utils.relDB
    for _, row in DB.iterrows():
        tutoreInfos = row['tutore']
        matiereRel = row['matiere']
        if tutoreInfos["nom"] == nom and tutoreInfos["prenom"] == prenom and matiereRel == matiere:
            return True, row["id"]
    return False, None


def buildIDList():
    DB = CoreLibs.utils.relDB
    global idList
    idList = list(DB.loc[:,"id"])
    return


def generateID():
    global idList
    for _ in range(5):
        generatedID = randint(0,(10**IDLEN)-1)
        if generatedID not in idList:
            idList.append(generatedID)
            return generatedID
    return False


def FusionnerDB(target):
    global idList
    if target == "":
        return ("Erreur", "Erreur: Aucun fichier selectionné",1)
    targetread = pandas.read_csv(file = target)
    with open(file="relations.csv") as mainDB:
        writer = csv.DictWriter(mainDB, fieldnames = ['id', 'Tuteur','Tutore','matiere','horaire'])
        for row in range(len(targetread)):
            if row["id"] in idList:
                pass
            else:
                writer.writerow(row)
                idList.append(row["id"])
    return


def getRelByID(id):
    if id not in idList:
        return False, None
    for _,row in CoreLibs.utils.relDB.iterrows():
        if row["id"] == id:
            return True, row
    return False, None


def getRelByTuteur(tuteur:tuple):
    DB = CoreLibs.utils.relDB
    for i in range(len(DB)):
        if DB.loc[i, "tuteur"] == str(tuteur):
            print(eval("DB.loc[i, 'tuteur'] == str(tuteur)"))
            return (DB.loc[i, "tutore"], DB.loc[i, "horaire"])
    horaire = "Aucune donnée"
    tutore = "Aucune donnée"
    return tutore, horaire
