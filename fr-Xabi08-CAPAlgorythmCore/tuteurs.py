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


def supprimerTuteur( nom, prn):
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
        if nomt.strip() == nom and prenomt.strip() == prn:
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


def doOtherChecks(i, nom, prn, niveau, dispos, matiere, niveaut):
    rels = []
    tuteursDB = CoreLibs.utils.tuteursDB
    if niveaut <= niveau:
        dispost = tuteursDB.loc[i,"disponibilites"]
    print(dispost)
    for j in range(len(dispos)):
        if dispos[j] in dispost:
            msg = "Un tuteur à été trouvé pour "+str(nom)+" "+str(prn)+" sur le créneau du "+str(creneaux[dispos[j]])+". Il s'agit de "+str(tuteursDB.loc[i,"nom"])+" "+str(tuteursDB.loc[i,"prenom"])+"."
            msg += "\n"
            rels.append({"tuteur":(tuteursDB.loc[i,"nom"],tuteursDB.loc[i,"prenom"]),"tutore": (nom, prn), "matiere": matiere, "horaire": dispos[j]})
    if rels != []:
        return True, rels, msg
    return False, None, None



##Fonction permettant de trouver les tuteurs
def trouverTuteur(nom, prn, niveau, matieres, dispos):
    tuteursDB = CoreLibs.utils.tuteursDB
    nbRelations = 0
    relationsTrouves = []
    for matiere in matieres:
        finalmsg = ""
        for i in range(len(tuteursDB)):
            niveaut = tuteursDB.loc[i,"niveau"]
            matieret = tuteursDB.loc[i,"matiere"]
            if "]" in matieret:
                matieret = matieret.split(",")
                print(matieret)
                for m in matieret:
                    m = m.replace("[","")
                    m = m.replace("]","")
                    m = m.replace("'","")
                    m = m.replace(" ","")
                    if m == matiere.replace(" ","") or (matiere == "Enseignement-scientifique SVT" and m == "SVT Spe") or (matiere == "Enseignement scientifique Physique" and m == "Physique Spe") or (matiere == "Mathematiques tronc-commun (TC)" and m == "Mathematiques"):
                        match, data, msg = doOtherChecks(i, nom, prn, niveau, dispos, matiere, niveaut)
                        if match:
                            print(data)
                            relationsTrouves+=data
                            finalmsg+=msg
                            nbRelations += 1
            else:
                matieret = matieret.strip()
                if matieret.strip() == matiere.strip() or (matiere == "Enseignement-scientifique SVT" and m == "SVT Spe") or (matiere == "Enseignement scientifique Physique" and m == "Physique Spe") or (matiere == "Mathematiques tronc-commun (TC)" and m == "Mathematiques"):
                    match, data, msg = doOtherChecks(i, nom, prn, niveau, dispos, matiere, niveaut)
                    if match:
                        relationsTrouves+=data
                        finalmsg+=msg
                        nbRelations += 1
    print(nbRelations)
    print(relationsTrouves)
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