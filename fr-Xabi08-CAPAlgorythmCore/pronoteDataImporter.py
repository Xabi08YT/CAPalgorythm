from pandas import read_csv
import csv
Corelibs = __import__('fr-Xabi08-CAPAlgorythmCore', globals(), locals(), ['basicDBCtrl','tuteurs','utils'])

#TODO IMPORTANT: formatage infos. PLUS IMPORTANT: Adapter les fieldnames à l'import des data Pronote 
def importFromDB(path,doRelationships):
    db = read_csv(path)
    Corelibs.basicDBCtrl.createDB('tutore.csv', ["nom","prenom","niveau","matieres","dispos"])
    with open(file = "tuteurs.csv", mode = 'a+',newline="") as database:
        windb = csv.DictWriter(database, ['nom', 'prenom','niveau','disponibilites','matiere','contact'])
        for r in range(len(db)):
            if db.loc[r,"tuteur"] == 1:
                Corelibs.tuteurs.ajouter({'nom': db.loc[r,"nom"], 'prenom': db.loc[r,"prenom"],'niveau': db.loc[r,"niveau"], 'disponibilites': db.loc[r,"dispos"],'matiere': db.loc[r,"matiereTuteur"]})
            if db.loc[r,"tutore"] == 1:
                row = {'nom': db.loc[r,'nom'], 'prenom': db.loc[r,"prenom"], 'niveau': db.loc[r,'niveau'], 'disponibilites': db.loc[r,"dispo"],'matiere': db.loc[r,'matiereTutore']}
                windb.writerow(row)
        database.close()    

        
        

#TODO: Do Rel automatically
def doRel():
    try:
        tutoreDB = read_csv('tutore.csv')
    except FileNotFoundError:
        return
    except Exception as e:
        Corelibs.utils.printInLogs(e,2)
        return