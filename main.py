import csv


def properexit(code):
    showinlog("Exiting with code " + str(code))
    quit(code)


def showinlog(message):
    with open("lastestlogs.txt", mode='a') as log:
        log.write(message)
    if "[STDFATAL]" in message:
        properexit(message)


def datastoretuteur(name, grade, disponibilites, matiere, contact):
    data = {'nom': name, 'niveau': grade, 'dispo': disponibilites, 'matiere': matiere, 'contact': contact}
    try:
        with open("tuteurs.csv", mode='a', newline='') as TFile:
            csvdatabase = csv.writer(TFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvdatabase.writerow([data])
    except FileNotFoundError:
        with open("tuteurs.csv", mode='x') as TFile:
            csvdatabase = csv.writer(TFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvdatabase.writerow(['Name'] + ['Niveau'] + ['Disponibilités'] + ['Matière'])
            showinlog("[STDINFO]: File tuteurs.csv couldn't be found. A New file name tuteurs.csv has been created.\n")
    return


def datacollectiontuteur():
    retry = True
    while retry:
        try:
            disponibilites = []
            dispmax = int(input("Entrez le nombre de créneaux disponibles du tuteur:"))
            nom = str(input("Entrez le nom du tuteur:"))
            niveau = str(input("Entrez le niveau du tuteur (2nde, 1ere ou Term):"))
            niveau = niveau.upper()
            for i in range(dispmax):
                temp = str(input(
                    "Entrez une disponibilité sous le format <2 premieres initales du jour><créneau horaire en partant de zéro>"))
                temp = temp.upper()
                disponibilites.append(temp)
            matiere = str(input("Entrez la matière dans lequel le tuteur veux aider:"))
            matiere = matiere.upper()
            contact = str(input("Veuillez entrer un moyen de contacter le tuteur."))
            datastoretuteur(nom, niveau, disponibilites, matiere, contact)
            return
        except ValueError:
            showinlog("[STDWARN]: User has entered wrong value type. Restarting data collection process...\n")
            return


def relationtuteurtutores():
    try:
        with open('tuteurs.csv', mode='r', newline='') as maindatabase:
            data = csv.reader(maindatabase)
            for row in data:
                print("CC".joinrow())
    except FileNotFoundError:
        return showinlog("[STDERR]: Please make a tutor database before using this.")

datacollectiontuteur()
properexit(0)
##relationtuteurtutores()
