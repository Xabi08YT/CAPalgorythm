import csv

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
            with open("tuteurs.csv", mode="r"):
                databse = csv.DictWriter()
                for row in databse:
                    if row["grade"] >= niveaututore:
                        if row["helping"] == matieredemandee:
                            dispotuteur = row["freehours"]
                            for i in range(nbdisptutore):
                                for j in range(row["freehoursnumb"]):
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