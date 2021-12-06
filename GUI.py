import tkinter
from tkinter import ttk
from tkinter import Radiobutton
import csv


# initialisation de l'interface graphique
interface = tkinter.Tk()
interface.title("Outil de gestion base de donnée CAPS")
interface.geometry("1440x1080")
interface.minsize(1080, 720)

lu0 = tkinter.StringVar()
lu0.set(0)
lu1 = tkinter.StringVar()
lu1.set(0)
lu2 = tkinter.StringVar()
lu2.set(0)
lu3 = tkinter.StringVar()
lu3.set(0)
lu4 = tkinter.StringVar()
lu4.set(0)
lu5 = tkinter.StringVar()
lu5.set(0)
lu6 = tkinter.StringVar()
lu6.set(0)
lu7 = tkinter.StringVar()
lu7.set(0)
lu8 = tkinter.StringVar()
lu8.set(0)
lu9 = tkinter.StringVar()
lu9.set(0)

ma0 = tkinter.StringVar()
ma0.set(0)
ma1 = tkinter.StringVar()
ma1.set(0)
ma2 = tkinter.StringVar()
ma2.set(0)
ma3 = tkinter.StringVar()
ma3.set(0)
ma4 = tkinter.StringVar()
ma4.set(0)
ma5 = tkinter.StringVar()
ma5.set(0)
ma6 = tkinter.StringVar()
ma6.set(0)
ma7 = tkinter.StringVar()
ma7.set(0)
ma8 = tkinter.StringVar()
ma8.set(0)
ma9 = tkinter.StringVar()
ma9.set(0)

me0 = tkinter.StringVar()
me0.set(0)
me1 = tkinter.StringVar()
me1.set(0)
me2 = tkinter.StringVar()
me2.set(0)
me3 = tkinter.StringVar()
me3.set(0)

je0 = tkinter.StringVar()
je0.set(0)
je1 = tkinter.StringVar()
je1.set(0)
je2 = tkinter.StringVar()
je2.set(0)
je3 = tkinter.StringVar()
je3.set(0)
je4 = tkinter.StringVar()
je4.set(0)
je5 = tkinter.StringVar()
je5.set(0)
je6 = tkinter.StringVar()
je6.set(0)
je7 = tkinter.StringVar()
je7.set(0)
je8 = tkinter.StringVar()
je8.set(0)
je9 = tkinter.StringVar()
je9.set(0)

ve0 = tkinter.StringVar()
ve0.set(0)
ve1 = tkinter.StringVar()
ve1.set(0)
ve2 = tkinter.StringVar()
ve2.set(0)
ve3 = tkinter.StringVar()
ve3.set(0)
ve4 = tkinter.StringVar()
ve4.set(0)
ve5 = tkinter.StringVar()
ve5.set(0)
ve6 = tkinter.StringVar()
ve6.set(0)
ve7 = tkinter.StringVar()
ve7.set(0)
ve8 = tkinter.StringVar()
ve8.set(0)
ve9 = tkinter.StringVar()
ve9.set(0)


def properexit(code):
    showinlog("Exiting with code " + str(code) + "\n")
    quit(code)


def showinlog(message):
    with open("lastestlogs.txt", mode='a') as log:
        log.write(message+str("\n"))
        log.close()
    if "[STDFATAL]" in message:
        return properexit(message)


def datastoretuteur(name, grade, disponibilites, matiere, contact):
    try:
        with open("tuteurs.csv", mode='a', newline='') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writeheader()
            csvdatabase.writerow({"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
            TFile.close()
    except FileNotFoundError:
        with open("tuteurs.csv", mode='x') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writeheader()
            csvdatabase.writerow(
                {"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
            showinlog("[STDINFO]: File tuteurs.csv couldn't be found. A New file name tuteurs.csv has been created.")
            TFile.close()
    else:
        showinlog("[STDERR]: Caouldn't write anything on database !")
    return


def modessplt(disp):
    showinlog("[STDINFO]: Determining mode to use...")
    nom = name_entry.get()
    niveau = niv.get()
    matiere = mat_list.get()
    contact = contact_entry.get()
    if modeout == True:
        datastoretuteur(nom, niveau, disp, matiere, contact)
    return showinlog("[STDINFO]: Done !")


def inforegroup(l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, mec0, mec1, mec2, mec3,
                J0, J1, J2, J3, J4, J5, J6, J7, J8, J9, V0, V1, V2, V3, V4, V5, V6, V7, V8, V9):
    lis = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, mec0, mec1, mec2, mec3, J0,
           J1, J2, J3, J4, J5, J6, J7, J8, J9, V0, V1, V2, V3, V4, V5, V6, V7, V8, V9]
    showinlog("[STDINFO]: Executing inforegroup function...")
    for k in range(len(lis)):
        try:
            if lis[k] == 0:
                lis.pop(0)
        except IndexError:
            showinlog("[STDWARN]: Index out of range !")
    showinlog("[STDINFO]: Done !")
    return lis


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
label_level = ttk.Label(mainframe,
                        text="Veuillez sélectionner le niveau (0 pour terminale, 1 pour première, 2 pour seconde) de la personne concernée.")

# Insertion de la barre permettant de choisir le niveau de la personne concernée
niv = tkinter.Scale(mainframe, from_=0, to=2, orient='horizontal')

# Insertion de la selection des horaires disponibles:
g_label = tkinter.Label(EDTFrame, text='Cochez les disponibilités de la personne concernée:')

j0_label = tkinter.Label(EDTFrame, text='Lundi')
LU0 = tkinter.Checkbutton(EDTFrame, onvalue='LU0', variable=lu0)
LU1 = tkinter.Checkbutton(EDTFrame, onvalue='LU1', variable=lu1)
LU2 = tkinter.Checkbutton(EDTFrame, onvalue='LU2', variable=lu2)
LU3 = tkinter.Checkbutton(EDTFrame, onvalue='LU3', variable=lu3)
LU4 = tkinter.Checkbutton(EDTFrame, onvalue='LU4', variable=lu4)
LU5 = tkinter.Checkbutton(EDTFrame, onvalue='LU5', variable=lu5)
LU6 = tkinter.Checkbutton(EDTFrame, onvalue='LU6', variable=lu6)
LU7 = tkinter.Checkbutton(EDTFrame, onvalue='LU7', variable=lu7)
LU8 = tkinter.Checkbutton(EDTFrame, onvalue='LU8', variable=lu8)
LU9 = tkinter.Checkbutton(EDTFrame, onvalue='LU9', variable=lu9)

j1_label = tkinter.Label(EDTFrame, text='Mardi')
MA0 = tkinter.Checkbutton(EDTFrame, onvalue='MA0', variable=ma0)
MA1 = tkinter.Checkbutton(EDTFrame, onvalue='MA1', variable=ma1)
MA2 = tkinter.Checkbutton(EDTFrame, onvalue='MA2', variable=ma2)
MA3 = tkinter.Checkbutton(EDTFrame, onvalue='MA3', variable=ma3)
MA4 = tkinter.Checkbutton(EDTFrame, onvalue='MA4', variable=ma4)
MA5 = tkinter.Checkbutton(EDTFrame, onvalue='MA5', variable=ma5)
MA6 = tkinter.Checkbutton(EDTFrame, onvalue='MA6', variable=ma6)
MA7 = tkinter.Checkbutton(EDTFrame, onvalue='MA7', variable=ma7)
MA8 = tkinter.Checkbutton(EDTFrame, onvalue='MA8', variable=ma8)
MA9 = tkinter.Checkbutton(EDTFrame, onvalue='MA9', variable=ma9)

j2_label = tkinter.Label(EDTFrame, text='Mercredi')
ME0 = tkinter.Checkbutton(EDTFrame, onvalue='ME0', variable=me0)
ME1 = tkinter.Checkbutton(EDTFrame, onvalue='ME1', variable=me1)
ME2 = tkinter.Checkbutton(EDTFrame, onvalue='ME2', variable=me2)
ME3 = tkinter.Checkbutton(EDTFrame, onvalue='ME3', variable=me3)

j3_label = tkinter.Label(EDTFrame, text='Jeudi')
JE0 = tkinter.Checkbutton(EDTFrame, onvalue='JE0', variable=je0)
JE1 = tkinter.Checkbutton(EDTFrame, onvalue='JE1', variable=je1)
JE2 = tkinter.Checkbutton(EDTFrame, onvalue='JE2', variable=je2)
JE3 = tkinter.Checkbutton(EDTFrame, onvalue='JE3', variable=je3)
JE4 = tkinter.Checkbutton(EDTFrame, onvalue='JE4', variable=je4)
JE5 = tkinter.Checkbutton(EDTFrame, onvalue='JE5', variable=je5)
JE6 = tkinter.Checkbutton(EDTFrame, onvalue='JE6', variable=je6)
JE7 = tkinter.Checkbutton(EDTFrame, onvalue='JE7', variable=je7)
JE8 = tkinter.Checkbutton(EDTFrame, onvalue='JE8', variable=je8)
JE9 = tkinter.Checkbutton(EDTFrame, onvalue='JE9', variable=je9)

j4_label = tkinter.Label(EDTFrame, text='Vendredi')
VE0 = tkinter.Checkbutton(EDTFrame, onvalue='VE0', variable=ve0)
VE1 = tkinter.Checkbutton(EDTFrame, onvalue='VE1', variable=ve1)
VE2 = tkinter.Checkbutton(EDTFrame, onvalue='VE2', variable=ve2)
VE3 = tkinter.Checkbutton(EDTFrame, onvalue='VE3', variable=ve3)
VE4 = tkinter.Checkbutton(EDTFrame, onvalue='VE4', variable=ve4)
VE5 = tkinter.Checkbutton(EDTFrame, onvalue='VE5', variable=ve5)
VE6 = tkinter.Checkbutton(EDTFrame, onvalue='VE6', variable=ve6)
VE7 = tkinter.Checkbutton(EDTFrame, onvalue='VE7', variable=ve7)
VE8 = tkinter.Checkbutton(EDTFrame, onvalue='VE8', variable=ve8)
VE9 = tkinter.Checkbutton(EDTFrame, onvalue='VE9', variable=ve9)

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
name_entry = tkinter.Entry(BottomFrame, width=30)
contact_label = tkinter.Label(BottomFrame, text="Entrez un moyen de contacter la personne:")
contact_entry = tkinter.Entry(BottomFrame, width=30)
mat_label = tkinter.Label(BottomFrame, text="Sélectionnez la matière de la personne:")
mat_list = ttk.Combobox(BottomFrame, values=Listematiere, width=30)

# insertion du bouton de validation et de loa progressbar
progbar = ttk.Progressbar(BottomFrame, mode="indeterminate", length=100)


def reset():
    showinlog("[STDINFO]: Reseting users choices...")
    LU0.deselect()
    LU1.deselect()
    LU2.deselect()
    LU3.deselect()
    LU4.deselect()
    LU5.deselect()
    LU6.deselect()
    LU7.deselect()
    LU8.deselect()
    LU9.deselect()

    MA0.deselect()
    MA1.deselect()
    MA2.deselect()
    MA3.deselect()
    MA4.deselect()
    MA5.deselect()
    MA6.deselect()
    MA7.deselect()
    MA8.deselect()
    MA9.deselect()

    ME0.deselect()
    ME1.deselect()
    ME2.deselect()
    ME3.deselect()

    JE0.deselect()
    JE1.deselect()
    JE2.deselect()
    JE3.deselect()
    JE4.deselect()
    JE5.deselect()
    JE6.deselect()
    JE7.deselect()
    JE8.deselect()
    JE9.deselect()

    VE0.deselect()
    VE1.deselect()
    VE2.deselect()
    VE3.deselect()
    VE4.deselect()
    VE5.deselect()
    VE6.deselect()
    VE7.deselect()
    VE8.deselect()
    VE9.deselect()
    name_entry.delete(0, "end")
    contact_entry.delete(0, "end")
    niv.set(0)
    mat_list.delete(0, "end")
    return showinlog("[STDINFO]: Done !")


def launch():
    showinlog("[STDINFO]: Executing program...")
    progbar.start()
    disponibilites = inforegroup(lu0, lu1, lu2, lu3, lu4, lu5, lu6, lu7, lu8, lu9, ma0, ma1, ma2, ma3, ma4, ma5, ma6,
                                 ma7, ma8, ma9, me0, me1, me2, me3, je0, je1, je2, je3, je4, je5, je6, je7, je8, je9,
                                 ve0, ve1, ve2, ve3, ve4, ve5, ve6, ve7, ve8, ve9)
    modessplt(disponibilites)
    progbar.stop()
    reset()
    showinlog("[STDINFO]: Done !")


validation = ttk.Button(BottomFrame, text="Valider", command=launch())
# Mise en page
label_blank = tkinter.Label(mainframe, text="        ")
label_blank1 = tkinter.Label(mainframe, text="        ")
label_blank2 = tkinter.Label(mainframe, text="        ")
label_blank3 = tkinter.Label(mainframe, text="        ")
label_blank4 = tkinter.Label(BottomFrame, text="        ")
label_blank5 = tkinter.Label(BottomFrame, text="        ")
label_blank6 = tkinter.Label(BottomFrame, text="            ")
label_blank7 = tkinter.Label(BottomFrame, text="            ")
label_blank8 = tkinter.Label(BottomFrame, text="            ")
label_blank9 = tkinter.Label(BottomFrame, text="            ")

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

name_label.grid(sticky='sw', column=0, row=3)
name_entry.grid(sticky='sw', column=0, row=4)
label_blank6.grid(sticky='sw', column=1, row=3)
contact_label.grid(sticky='sw', column=2, row=3)
contact_entry.grid(sticky='sw', column=2, row=4)
label_blank7.grid(sticky='sw', column=3, row=3)
mat_label.grid(sticky='sw', column=4, row=3)
mat_list.grid(sticky='sw', column=4, row=4)
label_blank8.grid(sticky='sw', column=5, row=3)
validation.grid(sticky='sw', column=6, row=4)
label_blank9.grid(sticky='sw', column=7, row=4)
progbar.grid(sticky='se', column=8, row=4)

# activation des frames:
mainframe.grid(sticky='n')
EDTFrame.grid(sticky='n', column=0, columnspan=6, row=4, rowspan=12)
BottomFrame.grid(sticky='s')

# activation de l'IUG
interface.mainloop()
