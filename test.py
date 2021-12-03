import csv
import tkinter


def properexit(code):
    showinlog("Exiting with code " + str(code))
    quit(code)


def showinlog(message):
    with open("lastestlogs.txt", mode='a') as log:
        log.write(message)


def datastoretuteur(name, grade, disponibilites, matiere, contact):
    try:
        with open("tuteurs.csv", mode='a', newline='') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writeheader()
            csvdatabase.writerow({"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
    except FileNotFoundError:
        with open("tuteurs.csv", mode='x') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writeheader()
            csvdatabase.writerow({"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
            showinlog("[STDINFO]: File tuteurs.csv couldn't be found. A New file name tuteurs.csv has been created.\n")
    return


def datacollectiontuteur():
    retry = True
    while retry == True:
        try:
            disponibilites = []
            dispmax = int(input("Entrez le nombre de créneaux disponibles du tuteur:"))
            nom = str(input("Entrez le nom du tuteur:"))
            niveau = int(input("Entrez 0 pour la terminale, 1 pour la 1ere et 2 pour la seconde."))
            for i in range(dispmax):
                temp = str(input(
                    "Entrez une disponibilité sous le format <2 premieres initales du jour><créneau horaire en partant de zéro>"))
                temp = temp.upper()
                disponibilites.append(temp)
            matiere = str(input("Entrez la matière dans lequel le tuteur veux aider:"))
            matiere = matiere.upper()
            contact = str(input("Veuillez entrer un moyen de contacter le tuteur."))
            datastoretuteur(nom, niveau, disponibilites, matiere, contact, dispmax)
            return
        except ValueError:
            showinlog("[STDWARN]: User has entered wrong value type. Restarting data collection process...\n")
    return


def reltuteurtutore():
    retry = True
    while retry:
        try:
            nbdisptutore = int(input("Entrez le nombre de créneaux horaire où le tutoré est disponible:"))
            nomtutore = str(input("Entrez le nom du tutoré:"))
            niveaututore = int(input("Entrez 0 pour la terminale, 1 pour la 1ere et 2 pour la seconde."))
            matieredemandee = str(input("Entrez la matiere où le tutoré souhaite être aidé."))
            disptutore = []
            for k in range(nbdisptutore):
                temp = str(input("Entrez une disponibilités du tutoré sous la forme <2 premiere lettre du jour en majuscule><numéro du créneau horaire compris entre 0 et 9 inclus>"))
                disptutore.append(temp)
            with open("tuteurs.csv", mode="r") as Data:
                database = csv.DictReader(Data, fieldnames=["name", "grade", "freehours", "helping", "contact"])
                for row in database:
                    if row["grade"] >= niveaututore:
                        if row["helping"] == matieredemandee:
                            dispotuteur = row["freehours"]
                            for i in range(nbdisptutore):
                                for j in range(len(dispotuteur)):
                                    if dispotuteur[j] == disptutore[j]:
                                        print("Diponibilité trouvée entre "+nomtutore+" et "+row["name"]+" sur le créneau horaire "+dispotuteur[j])
                                        garder = str(input("Voulez-vous garder cette correspondance?"))
                                        garder = garder.upper()
                                        if garder == "OUI":
                                            contact = row["contact"]
                                            contacttemp = contact.upper()
                                            if contacttemp == 'NONE' or contacttemp == 'AUCUN':
                                                return
                                            print("Voici un moyen de contacter le tuteur: "+contact)
                                            return
        except ValueError:
            print("Mauvais type de valeur entré. Redémarrage du processus de collecte d'information.")
        except KeyboardInterrupt:
            print("Opération interrompue.")
            retry = False
        except FileNotFoundError:
            print("Aucune base de données trouvée !")
    return

reltuteurtutore()

datacollectiontuteur()
properexit(0)

L = []
L.remove(1)