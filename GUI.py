import tkinter
from tkinter import ttk
from tkinter import Radiobutton
import csv

# initialisation de l'interface graphique
interface = tkinter.Tk()
interface.title("Outil de gestion base de donnée CAPS")
interface.geometry("1440x1080")
interface.minsize(1080, 720)


def properexit(code):
    showinlog("Exiting with code " + str(code) + "\n")
    quit(code)


def showinlog(message):
    with open("lastestlogs.txt", mode='a') as log:
        log.write(message)
    if "[STDFATAL]" in message:
        return properexit(message)


def datastoretuteur(name, grade, disponibilites, matiere, contact):
    try:
        with open("tuteurs.csv", mode='a', newline='') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writeheader()
            csvdatabase.writerow(
                {"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
    except FileNotFoundError:
        with open("tuteurs.csv", mode='x') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writeheader()
            csvdatabase.writerow(
                {"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
            showinlog("[STDINFO]: File tuteurs.csv couldn't be found. A New file name tuteurs.csv has been created.\n")
    return


def infoextract(disp):
    nom = name.get()
    niveau = niv.get()
    matiere = mat.get()
    contact = cont.get()
    if modeout == True:
        datastoretuteur(nom, niveau, disp, matiere, contact)
        return
    else:

        return

def dispregroupLU():
    Ludisp = []




# Initialisation des variables
modeout = tkinter.BooleanVar()
modeout.set(False)
name = tkinter.StringVar()
cont = tkinter.StringVar()
mat = tkinter.StringVar()
disp = []
Listematiere = ["Mathématiques", "Histoire-Géographie", "Education Morale et Civique", "Francais", "HGGSP", "NSI",
                "SNT(2nde)", "Physique-Chimie", "SVT", "Enseignement-scientifique", "Allemand", "Espagnol", "Anglais",
                "SES", "HLP", "Philosophie", "Litt. Anglaise"]

# initialisation des frames
mainframe = ttk.Frame(interface)
EDTFrame = ttk.Frame(interface)
BottomFrame = ttk.Frame(interface)

# ajout du premier texte
label_mode = ttk.Label(mainframe, text="Veuillez choisir le mode de fonctionnement de l'application:")

# Insertions des boutons de radio
modebtn1 = Radiobutton(mainframe, text="S'enregistrer en tant que tuteur.", variable=modeout, value=True)
modebtn2 = Radiobutton(mainframe, text="Trouver un tuteur", variable=modeout, value=False)

# ajout du deuxième texte
label_level = ttk.Label(mainframe,text="Veuillez sélectionner le niveau (0 pour terminale, 1 pour première, 2 pour seconde) de la personne concernée.")

# Insertion de la barre permettant de choisir le niveau de la personne concernée
niv = tkinter.Scale(mainframe, from_=0, to=2, orient='horizontal')

# Insertion de la selection des horaires disponibles:
g_label = tkinter.Label(EDTFrame, text='Cochez les disponibilités de la personne concernée:')

j0_label = tkinter.Label(EDTFrame, text='Lundi')
LU0 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU0')
LU1 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU1')
LU2 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU2')
LU3 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU3')
LU4 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU4')
LU5 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU5')
LU6 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU6')
LU7 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU7')
LU8 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU8')
LU9 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='LU9')

j1_label = tkinter.Label(EDTFrame, text='Mardi')
MA0 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA0')
MA1 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA1')
MA2 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA2')
MA3 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA3')
MA4 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA4')
MA5 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA5')
MA6 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA6')
MA7 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA7')
MA8 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA8')
MA9 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='MA9')

j2_label = tkinter.Label(EDTFrame, text='Mercredi')
ME0 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='ME0')
ME1 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='ME1')
ME2 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='ME2')
ME3 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='ME3')

j3_label = tkinter.Label(EDTFrame, text='Jeudi')
JE0 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE0')
JE1 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE1')
JE2 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE2')
JE3 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE3')
JE4 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE4')
JE5 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE5')
JE6 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE6')
JE7 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE7')
JE8 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE8')
JE9 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='JE9')

j4_label = tkinter.Label(EDTFrame, text='Vendredi')
VE0 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE0')
VE1 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE1')
VE2 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE2')
VE3 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE3')
VE4 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE4')
VE5 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE5')
VE6 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE6')
VE7 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE7')
VE8 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE8')
VE9 = tkinter.Checkbutton(EDTFrame, offvalue=' ', onvalue='VE9')

h0 = tkinter.Label(EDTFrame, text='8h10-8h05')
h1 = tkinter.Label(EDTFrame, text='9h05-10h')
h2 = tkinter.Label(EDTFrame, text='10h15-11h10')
h3 = tkinter.Label(EDTFrame, text='11h10-12h05')
h4 = tkinter.Label(EDTFrame, text='12h05-13h')
h5 = tkinter.Label(EDTFrame, text='13h-13h55')
h6 = tkinter.Label(EDTFrame, text='13h55-14h50')
h7 = tkinter.Label(EDTFrame, text='15h05-16h')
h8 = tkinter.Label(EDTFrame, text='16h-17h')
h9 = tkinter.Label(EDTFrame, text='17h-17h55')
pause = tkinter.Label(EDTFrame, text=" ")

# insertion des champs de saisie et du menu déroulant des matières
name_label = tkinter.Label(BottomFrame, text="Entrez le nom et le prénom de la personne:")
name_entry = tkinter.Entry(BottomFrame)
contact_label = tkinter.Label(BottomFrame, text="Entrez un moyen de contacter la personne:")
contact_entry = tkinter.Entry(BottomFrame)
mat_label = tkinter.Label(BottomFrame, text="Sélectionnez la matière de la personne.")
mat_list = ttk.Combobox(BottomFrame, values=Listematiere)

# Mise en page
label_blank = tkinter.Label(mainframe, text="        ")
label_blank1 = tkinter.Label(mainframe, text="        ")
label_blank2 = tkinter.Label(mainframe, text="        ")
label_blank3 = tkinter.Label(mainframe, text="        ")
label_blank4 = tkinter.Label(BottomFrame, text="        ")
label_blank5 = tkinter.Label(BottomFrame, text="        ")

label_mode.grid(column=0, columnspan=3, row=0)
modebtn1.grid(column=0, columnspan=1, row=1, sticky='w')
modebtn2.grid(column=0, columnspan=1, row=2, sticky='w')

label_blank.grid(column=4, row=0, columnspan=1)
label_blank1.grid(column=5, row=0, columnspan=1)
label_blank2.grid(column=6, row=0, columnspan=1)

label_level.grid(column=7, row=0, columnspan=5)
niv.grid(column=7, row=1)

label_blank3.grid(columnspan=10, column=0, row=3)

g_label.grid(sticky='n')

h0.grid(column=0, row=2, sticky='w')
h1.grid(column=0, row=3, sticky='w')
h2.grid(column=0, row=4, sticky='w')
h3.grid(column=0, row=5, sticky='w')
h4.grid(column=0, row=6, sticky='w')
h5.grid(column=0, row=8, sticky='w')
h6.grid(column=0, row=9, sticky='w')
h7.grid(column=0, row=10, sticky='w')
h8.grid(column=0, row=11, sticky='w')
h9.grid(column=0, row=12, sticky='w')

j0_label.grid(column=1, row=1)
LU0.grid(column=1, columnspan=1, row=2)
LU1.grid(column=1, columnspan=1, row=3)
LU2.grid(column=1, columnspan=1, row=4)
LU3.grid(column=1, columnspan=1, row=5)
LU4.grid(column=1, columnspan=1, row=6)
pause.grid(column=0, columnspan=6, row=7)
LU5.grid(column=1, columnspan=1, row=8)
LU6.grid(column=1, columnspan=1, row=9)
LU7.grid(column=1, columnspan=1, row=10)
LU8.grid(column=1, columnspan=1, row=11)
LU9.grid(column=1, columnspan=1, row=12)

j1_label.grid(column=2, row=1)
MA0.grid(column=2, columnspan=1, row=2)
MA1.grid(column=2, columnspan=1, row=3)
MA2.grid(column=2, columnspan=1, row=4)
MA3.grid(column=2, columnspan=1, row=5)
MA4.grid(column=2, columnspan=1, row=6)
MA5.grid(column=2, columnspan=1, row=8)
MA6.grid(column=2, columnspan=1, row=9)
MA7.grid(column=2, columnspan=1, row=10)
MA8.grid(column=2, columnspan=1, row=11)
MA9.grid(column=2, columnspan=1, row=12)

j2_label.grid(column=3, row=1)
ME0.grid(column=3, columnspan=1, row=2)
ME1.grid(column=3, columnspan=1, row=3)
ME2.grid(column=3, columnspan=1, row=4)
ME3.grid(column=3, columnspan=1, row=5)

j3_label.grid(column=4, row=1)
JE0.grid(column=4, columnspan=1, row=2)
JE1.grid(column=4, columnspan=1, row=3)
JE2.grid(column=4, columnspan=1, row=4)
JE3.grid(column=4, columnspan=1, row=5)
JE4.grid(column=4, columnspan=1, row=6)
JE5.grid(column=4, columnspan=1, row=8)
JE6.grid(column=4, columnspan=1, row=9)
JE7.grid(column=4, columnspan=1, row=10)
JE8.grid(column=4, columnspan=1, row=11)
JE9.grid(column=4, columnspan=1, row=12)

j4_label.grid(column=5, row=1)
VE0.grid(column=5, columnspan=1, row=2)
VE1.grid(column=5, columnspan=1, row=3)
VE2.grid(column=5, columnspan=1, row=4)
VE3.grid(column=5, columnspan=1, row=5)
VE4.grid(column=5, columnspan=1, row=6)
VE5.grid(column=5, columnspan=1, row=8)
VE6.grid(column=5, columnspan=1, row=9)
VE7.grid(column=5, columnspan=1, row=10)
VE8.grid(column=5, columnspan=1, row=11)
VE9.grid(column=5, columnspan=1, row=12)

label_blank4.grid(column=0, row=15)
label_blank5.grid(column=0, row=16)

name_label.grid(sticky='sw')
name_entry.grid(sticky='sw')
contact_label.grid(sticky='sw')
contact_entry.grid(sticky='sw')
mat_label.grid(sticky='sw')
mat_list.grid(sticky='sw')

# activation des frames:
mainframe.grid(sticky='n')
EDTFrame.grid(sticky='n', column=0, columnspan=6, row=4, rowspan=12)
BottomFrame.grid(sticky='s')

# activation de l'IUG
interface.mainloop()