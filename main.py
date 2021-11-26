from tkinter import *
from os import *



def basicdatainput():
    retry = True
    essais = 0
    while retry == True:
        try:
            tuteur = bool(input("Veuillez dire si la peronne est un tuteur. Si oui, mettre True en respectant la casse, sinon mettre False en respectant aussi la casse."))
            retry = False
        except ValueError:
            print("Une erreur est survenue. Veuillez réessayer.")
            essais += 1
        if essais == 3:
            temp = upper(str(input("Voulez-vous réessayer?")))
            if temp == 'NON':
                retry = False
                return
            
    if tuteur == True:
        nom = str(input("Entrez le nom de la personne"))
        classe = str(input("Entrez le niveau du tuteur."))
    return(nom, classe)

def disponibilites():
    