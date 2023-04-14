import pandas
import os
import csv

CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["basicDBCtrl", "utils"],0)

def estDansBase(row):
    tuteursDB = CoreLibs.utils.tuteursDB
    print(tuteursDB)
    if len(tuteursDB) == 0:
        return False
    for r in range(len(tuteursDB)):
        nomr = tuteursDB.loc[r, "nom"]
        prenomr = tuteursDB.loc[r, "prenom"]
        niveaur = tuteursDB.loc[r, "niveau"]
        disposr = tuteursDB.loc[r, "disponibilites"]
        print(row["disponibilites"],disposr)
        matierer = tuteursDB.loc[r, "matiere"]
        print(row["nom"].strip() == nomr.strip())
        print(row["prenom"] == prenomr.strip())
        print(row["niveau"] == niveaur)
        print(row["matiere"] == matierer.strip())
        print(row["nom"].strip() == nomr.strip() and row["prenom"] == prenomr.strip() and row["niveau"] == niveaur and row["matiere"] == matierer.strip())
        if row["nom"].strip() == nomr.strip() and row["prenom"] == prenomr.strip() and row["niveau"] == niveaur and row["matiere"] == matierer.strip():
            return True
    return False


def supprimerTuteur( nom, prn, matiere):
    tuteursDB = CoreLibs.utils.tuteursDB
    print("suppression...") 
    ligneASupprimer = None
    print(len(tuteursDB))
    if len(tuteursDB) == 0:
        return ("Erreur de base de donnees", "Erreur: Impossible de supprimer une information d'une base de données vide",1)
    print("debug1")
    for i in range(len(tuteursDB)):
        print(i)
        nomt = tuteursDB.loc[i, "nom"]
        prenomt = tuteursDB.loc[i, "prenom"]
        matieret = tuteursDB.loc[i, "matiere"]
        print(nomt.strip() == nom and prenomt.strip() == prn and matieret.strip() == matiere)
        if nomt.strip() == nom and prenomt.strip() == prn and matieret.strip() == matiere:
            ligneASupprimer = i
            break
    print("debug2")
    tuteursDBTemp = tuteursDB.copy()
    os.remove(path = "tuteurs.csv")
    with open(file="tuteurs.csv", mode="a+",newline="") as temp:
        tempw = csv.DictWriter(temp, fieldnames = ['nom', 'prenom','niveau','disponibilites','matiere','contact'])
        tempw.writeheader()
        for j in range(len(tuteursDBTemp)):
            if j != ligneASupprimer:
                tempw.writerow({"nom": str(tuteursDBTemp.loc[j,"nom"]).strip(), "prenom": str(tuteursDBTemp.loc[j,"prenom"]).strip(), "niveau": tuteursDBTemp.loc[j,"niveau"], "disponibilites": tuteursDBTemp.loc[j,"disponibilites"], "matiere": str(tuteursDBTemp.loc[j,"matiere"]).strip(), "contact": str(tuteursDBTemp.loc[j,"contact"]).strip()})
        temp.close()
    CoreLibs.utils.actualiserDB()
    return


def FusionnerDB(target):
    if target == "":
        return ("Erreur", "Erreur: Aucun fichier selectionné",1)
    targetread = pandas.read_csv(file = target)
    with open(file="tuteurs.csv") as mainDB:
        writer = csv.DictWriter(mainDB, fieldnames = ['nom', 'prenom','niveau','disponibilites','matiere','contact'])
        for rows in targetread:
            if estDansBase(rows):
                pass
            else:
                writer.writerow(rows)
    return


##Fonction permettant de trouver les tuteurs
def trouverTuteur(nom, prn, niveau, matiere, dispos):
    tuteursDB = CoreLibs.utils.tuteursDB
    nbRelations = 0
    relationsTrouves = []
    finalmsg = ""
    creneaux = {"LU0": "Lundi de 8h à 9h","LU1": "Lundi de 9h à 10h","LU2": "Lundi de 10h à 11h","LU3": "Lundi de 11h à 12h","LU4": "Lundi de 12h à 13h","LU5": "Lundi de 13h à 14h","LU6": "Lundi de 14h à 15h","LU7": "Lundi de 15h à 16h","LU8": "Lundi de 16h à 17h","LU9":"Lundi de 17h à 18h",
                "MA0": "Mardi de 8h à 9h","MA1": "Mardi de 9h à 10h","MA2": "Mardi de 10h à 11h","MA3": "Mardi de 11h à 12h","MA4": "Mardi de 12h à 13h","MA5": "Mardi de 13h à 14h","MA6": "Mardi de 14h à 15h","MA7": "Mardi de 15h à 16h","MA8": "Mardi de 16h à 17h","MA9":"Mardi de 17h à 18h",
                "ME0": "Mercredi de 8h à 9h","ME1": "Mercredi de 9h à 10h","ME2": "Mercredi de 10h à 11h","ME3": "Mercredi de 11h à 12h",
                "JE0": "Jeudi de 8h à 9h","JE1": "Jeudi de 9h à 10h","JE2": "Jeudi de 10h à 11h","JE3": "Jeudi de 11h à 12h","JE4": "Jeudi de 12h à 13h","JE5": "Jeudi de 13h à 14h","JE6": "Jeudi de 14h à 15h","JE7": "Jeudi de 15h à 16h","JE8": "Jeudi de 16h à 17h","JE9":"Jeudi de 17h à 18h",
                "VE0": "Vendredi de 8h à 9h","VE1": "Vendredi de 9h à 10h","VE2": "Vendredi de 10h à 11h","VE3": "Vendredi de 11h à 12h","VE4": "Vendredi de 12h à 13h","VE5": "Vendredi de 13h à 14h","VE6": "Vendredi de 14h à 15h","VE7": "Vendredi de 15h à 16h","VE8": "Vendredi de 16h à 17h","VE9":"Vendredi de 17h à 18h",}
    for i in range(len(tuteursDB)):
        matieret = str(tuteursDB.loc[i,"matiere"])
        niveaut = tuteursDB.loc[i,"niveau"]
        matieret = matieret.strip()
        print(matieret)
        print(niveaut)
        print(eval("matieret == matiere"))
        if matieret.strip() == matiere.strip() and niveaut <= niveau or (matiere == "Enseignement-scientifique SVT" and matieret == "SVT Spe") or (matiere == "Enseignement scientifique Physique" and matieret == "Physique Spe"):
            dispost = tuteursDB.loc[i,"disponibilites"]
            print(dispost)
            for j in range(len(dispos)):
                if dispos[j] in dispost:
                    msg = "Un tuteur à été trouvé pour "+str(nom)+" "+str(prn)+" sur le créneau du "+str(creneaux[dispos[j]])+". Il s'agit de "+str(tuteursDB.loc[i,"nom"])+" "+str(tuteursDB.loc[i,"prenom"])+"."
                    finalmsg = finalmsg +msg+"\n"
                    relationsTrouves.append({"Tuteur":(tuteursDB.loc[i,"nom"],tuteursDB.loc[i,"prenom"]),"Tutore": (nom, prn), "Matiere": matiere, "horaire": dispos[j]})
                nbRelations += 1
    if nbRelations == 0:
        return ("Information","Aucune relation n'a été trouvée.", 1), None, None
    if nbRelations == 1:
        return ("Information", finalmsg, 1), relationsTrouves, 1
    return ("Information", finalmsg, 1), relationsTrouves, 2