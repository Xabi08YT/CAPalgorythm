from tkinter import *
from os import *
from typing import final

datafile = open('data.txt', 'r')

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
            if temp == 'NON':
                retry = False
                return
            
    if tuteur == True:
        nom = str(input("Entrez le nom de la personne"))
        niveau = str(input("Entrez le niveau du tuteur."))
        datafile = open('data.txt', 'w')

    return(nom, niveau)

def properexit():
    close('data.txt')
    close('output.xls')
    quit(0)