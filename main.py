from tkinter import *
from os import *
from typing import final

logfile = open('lastest-logs.txt', mode='w')

def properexit():
    close('data.txt')
    close('output.xls')
    quit(0)

def showinlog(message):
    with open(logfile):
        write(message)


try:
    datafile = open('data.txt', mode='w')
except Exception:
    showinlog("Erreur lors de l'ouverture du fichier de données.")

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
            temp = str(input("Voulez-vous réessayer?"))
            if temp == ('NON' or 'Non' or 'NOn' or 'NoN' or 'nOn'or 'NON'):
                retry = False
                return
            
    if tuteur == True:
        nom = str(input("Entrez le nom de la personne"))
        niveau = str(input("Entrez le niveau du tuteur."))
        datafile = open('data.txt', 'w')

    return(nom, niveau)
