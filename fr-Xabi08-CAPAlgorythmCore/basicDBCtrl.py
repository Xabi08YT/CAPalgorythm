import csv
import os

def resetDB():
    os.remove(path = 'tuteurs.csv')
    createDB('tuteurs.csv', fieldnames = ['nom', 'prenom','niveau','disponibilites','matiere','contact'])
    try:
        os.remove(path = 'relations.csv')
        createDB("relations.csv", fieldnames=['id', 'Tuteur','Tutore','matiere','horaire'])
        os.remove(path = "feedback.csv")
        createDB("feedback.csv", fieldnames=["feedbackid","tutore","tuteur","caractere","matiere","efficacite","idrelation","commentaires"])
    except FileNotFoundError:
        pass
    return ("Information","Bases de données réinitialisées avec succès.", 1)


def createDB(name:str,fieldnames:list, dataToWrite:list = []):
    """
    Création automatique de base de données CSV avec écriture de ligne possible
    name: Nom de la DB
    fieldnames: nom des colones
    dataToWrite: Données à écrire
    Ne retourne rien.
    """
    with open(file=name, mode="a+",newline="") as temp:
        tempw = csv.DictWriter(temp, fieldnames = fieldnames)
        tempw.writeheader()
        for line in dataToWrite:
            tempw.writerow(line)
        temp.close()
    return


def editConfig(logsOpt,feedbackOpt,RelDB):
    print(logsOpt, feedbackOpt, RelDB)
    os.remove(path="config.csv")
    createDB("config.csv",["properties","state"], [{"properties": "enableLogs", "state": logsOpt},{"properties": "enableFeedback", "state": feedbackOpt},{"properties": "enableRelDB", "state": RelDB}])
    return
