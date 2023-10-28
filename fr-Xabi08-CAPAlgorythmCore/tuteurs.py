import os

CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["basicDBCtrl", "utils"],0)


creneaux = CoreLibs.utils.creneaux


def supprimerTuteur(nom, prn, classe):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("DELETE FROM tuteur INNER JOIN group ON group.id = tuteur.group WHERE name = ? AND surname = ? AND groups.label = ?" (nom,prn,classe))
    MainDB.commit()
    return


def FusionnerDB(target):
    if target == "":
        return ("Erreur", "Erreur: Aucun fichier selectionné",1)
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
    results = []
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    for m in len(matieres):
        matieres[m] = "%"+matieres[m]+"%"
        for i in len(dispos):
            check = "%"+dispos[i]+"%"
            cursor.execute(""""SELECT nom, prenom FROM tuteur WHERE tuteur.grade >= ? AND freeon LIKE ? AND subject LIKE ?""",(niveau,check,matieres[m]))
            results.append(cursor.fetchall())
    nbRelations = len(results)
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