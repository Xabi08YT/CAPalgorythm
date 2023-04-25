from random import randint
import csv
import unidecode
import pandas
from os import remove
CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils","relations"],0)


IDLEN = 10
idList = []


def ajouterFeedback(efficacite:int, caractere:int, relID:int, temporary:bool, commentaires:str, id:int = -1):
    idrelation = ""
    commentaires = unidecode.unidecode(commentaires)
    CoreLibs.relations.getRelByID(relID)
    if idList == []:
        buildIDList()
    relInfos = CoreLibs.relations.getRelByID()
    if temporary:
        idrelation = relID
    if id == -1:
        feedbackid = generateID()
    else: 
        feedbackid = id
    with open("feedback.csv", mode = "a+") as f:
        writer = csv.DictWriter(f, fieldnames=["feedbackid","tutore","tuteur","caractere","matiere","efficacite","idrelation","commentaire"])
        writer.writerow({"feedbackid": feedbackid,"tutore": relInfos["tutore"],"tuteur": relInfos["tuteur"], "caractere": caractere,"matiere": relInfos["matiere"],"efficacite":efficacite,"idrelation":idrelation, "commentaires": commentaires})
        f.close()
    return
        

def buildIDList():
    DB = CoreLibs.utils.feedback
    global idList
    idList = DB.loc[:,"id"]
    return


def generateID():
    global idList
    for _ in range(5):
        generatedID = randint(0,(10**IDLEN)-1)
        if generatedID not in idList:
            idList.append(generatedID)
            return generatedID
    return False


def removeFeedbackByID(id):
    DB = CoreLibs.utils.feedback
    index = None
    for i, row in DB.iterrows():
        if id == row["feedbackid"]:
            index = i
    _feedbacks = DB.copy()
    remove("feedback.csv")
    with open(file="feedback.csv", mode="a+",newline="") as temp:
        tempw = csv.DictWriter(temp, fieldnames = ["feedbackid","tutore","tuteur","caractere","matiere","efficacite","idrelation","commentaires"])
        tempw.writeheader()
        for j in range(len(_feedbacks)):
            if j != index:
                tempw.writerow({"id": _feedbacks.loc[j,"feedbackid"], "tutore": str(_feedbacks.loc[j,"tutore"]).strip(), "tuteur":str(_feedbacks.loc["tuteur"]),"caractere":_feedbacks.loc[j,"caractere"],"matiere": str(_feedbacks.loc[j,"matiere"]).strip(), "efficacite": _feedbacks.loc[j,"efficacite"], "idrelation": _feedbacks.loc[j,"idrelation"],"commentaires":_feedbacks.loc[j, "commentaires"]})
        temp.close()


def replaceFeedback(id, efficacite:int, caractere:int, relID:int, temporary:bool, commentaires:str):
    removeFeedbackByID(id)
    ajouterFeedback(efficacite, caractere, relID, temporary, commentaires)
    return


def getFeedbackIdByRelID(relID):
    DB = CoreLibs.utils.feedback
    for _,row in DB.iterrows():
        if relID == row["idrelation"]:
            return row["feedbackid"]
    return None


def FusionnerDB(target):
    global idList
    if target == "":
        return ("Erreur", "Erreur: Aucun fichier selectionné",1)
    targetread = pandas.read_csv(file = target)
    with open(file="feedback.csv") as mainDB:
        writer = csv.DictWriter(mainDB, fieldnames = ["feedbackid","tutore","tuteur","caractere","matiere","efficacite","idrelation","commentaires"])
        for row in range(len(targetread)):
            if row["feedbackid"] in idList:
                pass
            else:
                writer.writerow(row)
                idList.append(row["feedbackid"])
    return


def getFeedbackByUsers(tuteur:tuple,tutore:tuple):
    DB = CoreLibs.utils.feedback
    tuteur = str(tuteur)
    tutore = str(tutore)
    try:
        efficacite = DB.efficacite[(DB.tuteur == tuteur) & (DB.tutore == tutore)]
        caractere = [(DB.tuteur == tuteur) & (DB.tutore == tutore)]
    except Exception as e:
        print(e)
        efficacite = "Aucune donnée"
        caractere = "Aucune donnée"
    return efficacite, caractere