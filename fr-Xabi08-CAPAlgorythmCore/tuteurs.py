import pandas
import os
import csv

CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["basicDBCtrl", "utils"],0)

creneaux = CoreLibs.utils.creneaux

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
                    relationsTrouves.append({"tuteur":(tuteursDB.loc[i,"nom"],tuteursDB.loc[i,"prenom"]),"tutore": (nom, prn), "matiere": matiere, "horaire": dispos[j]})
                nbRelations += 1
    if nbRelations == 0:
        return ("Information","Aucune relation n'a été trouvée.", 1), None, None
    if nbRelations == 1:
        return ("Information", finalmsg, 1), relationsTrouves, 1
    return ("Information", finalmsg, 1), relationsTrouves, 2


def ajouter(row):
    with open(file = "tuteurs.csv", mode = 'a+',newline="") as database:
        windb = csv.DictWriter(database, ['nom', 'prenom','niveau','disponibilites','matiere','contact'])
        windb.writerow(row)
        database.close()