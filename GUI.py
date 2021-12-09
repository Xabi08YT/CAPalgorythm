import time
import tkinter
from tkinter import ttk
from tkinter import Radiobutton
import csv
import datetime

# initialisation de l'interface graphique
interface = tkinter.Tk()
interface.title("Interface base de données CAPS")
interface.geometry("1440x1080")
interface.minsize(1080, 720)

lu0 = tkinter.IntVar()
lu0.set(0)
lu1 = tkinter.IntVar()
lu1.set(0)
lu2 = tkinter.IntVar()
lu2.set(0)
lu3 = tkinter.IntVar()
lu3.set(0)
lu4 = tkinter.IntVar()
lu4.set(0)
lu5 = tkinter.IntVar()
lu5.set(0)
lu6 = tkinter.IntVar()
lu6.set(0)
lu7 = tkinter.IntVar()
lu7.set(0)
lu8 = tkinter.IntVar()
lu8.set(0)
lu9 = tkinter.IntVar()
lu9.set(0)

ma0 = tkinter.IntVar()
ma0.set(0)
ma1 = tkinter.IntVar()
ma1.set(0)
ma2 = tkinter.IntVar()
ma2.set(0)
ma3 = tkinter.IntVar()
ma3.set(0)
ma4 = tkinter.IntVar()
ma4.set(0)
ma5 = tkinter.IntVar()
ma5.set(0)
ma6 = tkinter.IntVar()
ma6.set(0)
ma7 = tkinter.IntVar()
ma7.set(0)
ma8 = tkinter.IntVar()
ma8.set(0)
ma9 = tkinter.IntVar()
ma9.set(0)

me0 = tkinter.IntVar()
me0.set(0)
me1 = tkinter.IntVar()
me1.set(0)
me2 = tkinter.IntVar()
me2.set(0)
me3 = tkinter.IntVar()
me3.set(0)

je0 = tkinter.IntVar()
je0.set(0)
je1 = tkinter.IntVar()
je1.set(0)
je2 = tkinter.IntVar()
je2.set(0)
je3 = tkinter.IntVar()
je3.set(0)
je4 = tkinter.IntVar()
je4.set(0)
je5 = tkinter.IntVar()
je5.set(0)
je6 = tkinter.IntVar()
je6.set(0)
je7 = tkinter.IntVar()
je7.set(0)
je8 = tkinter.IntVar()
je8.set(0)
je9 = tkinter.IntVar()
je9.set(0)

ve0 = tkinter.IntVar()
ve0.set(0)
ve1 = tkinter.IntVar()
ve1.set(0)
ve2 = tkinter.IntVar()
ve2.set(0)
ve3 = tkinter.IntVar()
ve3.set(0)
ve4 = tkinter.IntVar()
ve4.set(0)
ve5 = tkinter.IntVar()
ve5.set(0)
ve6 = tkinter.IntVar()
ve6.set(0)
ve7 = tkinter.IntVar()
ve7.set(0)
ve8 = tkinter.IntVar()
ve8.set(0)
ve9 = tkinter.IntVar()
ve9.set(0)

# Initialisation des variables
modeout = tkinter.IntVar()
modeout.set(1)
name = tkinter.StringVar()
cont = tkinter.StringVar()
mat = tkinter.StringVar()
nivvar = tkinter.IntVar()
nivvar.set(0)
Listematiere = ["Mathématiques", "Histoire-Géographie", "Education Morale et Civique", "Francais", "HGGSP", "NSI",
                "SNT(2nde)", "Physique-Chimie", "SVT", "Enseignement-scientifique", "Allemand", "Espagnol", "Anglais",
                "SES", "HLP", "Philosophie", "Litt. Anglaise"]


# initialisation des frames
mainframe = ttk.Frame(interface)
EDTFrame = ttk.Frame(interface)
BottomFrame = ttk.Frame(interface)

# ajout du premier texte
label_mode = ttk.Label(mainframe, text="Veuillez choisir le mode de fonctionnement de l'application:")





# ajout du deuxième texte
label_level = ttk.Label(mainframe, text="Veuillez sélectionner le niveau (0 pour terminale, 1 pour première, 2 pour seconde) de la personne concernée.")

# Insertion de la barre permettant de choisir le niveau de la personne concernée
niv = tkinter.Scale(mainframe, from_=0, to=2, orient='horizontal', variable=nivvar)

# Insertion de la selection des horaires disponibles:
g_label = tkinter.Label(EDTFrame, text='Cochez les disponibilités de la personne concernée:')

j0_label = tkinter.Label(EDTFrame, text='Lundi')
LU0 = tkinter.Checkbutton(EDTFrame, variable=lu0)
LU1 = tkinter.Checkbutton(EDTFrame, variable=lu1)
LU2 = tkinter.Checkbutton(EDTFrame, variable=lu2)
LU3 = tkinter.Checkbutton(EDTFrame, variable=lu3)
LU4 = tkinter.Checkbutton(EDTFrame, variable=lu4)
LU5 = tkinter.Checkbutton(EDTFrame, variable=lu5)
LU6 = tkinter.Checkbutton(EDTFrame, variable=lu6)
LU7 = tkinter.Checkbutton(EDTFrame, variable=lu7)
LU8 = tkinter.Checkbutton(EDTFrame, variable=lu8)
LU9 = tkinter.Checkbutton(EDTFrame, variable=lu9)

j1_label = tkinter.Label(EDTFrame, text='Mardi')
MA0 = tkinter.Checkbutton(EDTFrame, variable=ma0)
MA1 = tkinter.Checkbutton(EDTFrame, variable=ma1)
MA2 = tkinter.Checkbutton(EDTFrame, variable=ma2)
MA3 = tkinter.Checkbutton(EDTFrame, variable=ma3)
MA4 = tkinter.Checkbutton(EDTFrame, variable=ma4)
MA5 = tkinter.Checkbutton(EDTFrame, variable=ma5)
MA6 = tkinter.Checkbutton(EDTFrame, variable=ma6)
MA7 = tkinter.Checkbutton(EDTFrame, variable=ma7)
MA8 = tkinter.Checkbutton(EDTFrame, variable=ma8)
MA9 = tkinter.Checkbutton(EDTFrame, variable=ma9)

j2_label = tkinter.Label(EDTFrame, text='Mercredi')
ME0 = tkinter.Checkbutton(EDTFrame, variable=me0)
ME1 = tkinter.Checkbutton(EDTFrame, variable=me1)
ME2 = tkinter.Checkbutton(EDTFrame, variable=me2)
ME3 = tkinter.Checkbutton(EDTFrame, variable=me3)

j3_label = tkinter.Label(EDTFrame, text='Jeudi')
JE0 = tkinter.Checkbutton(EDTFrame, variable=je0)
JE1 = tkinter.Checkbutton(EDTFrame, variable=je1)
JE2 = tkinter.Checkbutton(EDTFrame, variable=je2)
JE3 = tkinter.Checkbutton(EDTFrame, variable=je3)
JE4 = tkinter.Checkbutton(EDTFrame, variable=je4)
JE5 = tkinter.Checkbutton(EDTFrame, variable=je5)
JE6 = tkinter.Checkbutton(EDTFrame, variable=je6)
JE7 = tkinter.Checkbutton(EDTFrame, variable=je7)
JE8 = tkinter.Checkbutton(EDTFrame, variable=je8)
JE9 = tkinter.Checkbutton(EDTFrame,  variable=je9)

j4_label = tkinter.Label(EDTFrame, text='Vendredi')
VE0 = tkinter.Checkbutton(EDTFrame, variable=ve0)
VE1 = tkinter.Checkbutton(EDTFrame, variable=ve1)
VE2 = tkinter.Checkbutton(EDTFrame, variable=ve2)
VE3 = tkinter.Checkbutton(EDTFrame, variable=ve3)
VE4 = tkinter.Checkbutton(EDTFrame, variable=ve4)
VE5 = tkinter.Checkbutton(EDTFrame, variable=ve5)
VE6 = tkinter.Checkbutton(EDTFrame, variable=ve6)
VE7 = tkinter.Checkbutton(EDTFrame, variable=ve7)
VE8 = tkinter.Checkbutton(EDTFrame, variable=ve8)
VE9 = tkinter.Checkbutton(EDTFrame, variable=ve9)

h0 = tkinter.Label(EDTFrame, text='8h10-9h05')
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
name_entry = tkinter.Entry(BottomFrame, width=30, textvariable=name)
contact_label = tkinter.Label(BottomFrame, text="Entrez un moyen de contacter la personne: (factultatif)")
contact_entry = tkinter.Entry(BottomFrame, width=30, textvariable=cont)
mat_label = tkinter.Label(BottomFrame, text="Sélectionnez la matière de la personne:")
mat_list = ttk.Combobox(BottomFrame, values=Listematiere, width=30, textvariable=mat)



# Insertions des boutons de radio


def controlstateEn():
    LU0.config(state='normal')
    LU1.config(state='normal')
    LU2.config(state='normal')
    LU3.config(state='normal')
    LU4.config(state='normal')
    LU5.config(state='normal')
    LU6.config(state='normal')
    LU7.config(state='normal')
    LU8.config(state='normal')
    LU9.config(state='normal')

    MA0.config(state='normal')
    MA1.config(state='normal')
    MA2.config(state='normal')
    MA3.config(state='normal')
    MA4.config(state='normal')
    MA5.config(state='normal')
    MA6.config(state='normal')
    MA7.config(state='normal')
    MA8.config(state='normal')
    MA9.config(state='normal')

    ME0.config(state='normal')
    ME1.config(state='normal')
    ME2.config(state='normal')
    ME3.config(state='normal')

    JE0.config(state='normal')
    JE1.config(state='normal')
    JE2.config(state='normal')
    JE3.config(state='normal')
    JE4.config(state='normal')
    JE5.config(state='normal')
    JE6.config(state='normal')
    JE7.config(state='normal')
    JE8.config(state='normal')
    JE9.config(state='normal')

    VE0.config(state='normal')
    VE1.config(state='normal')
    VE2.config(state='normal')
    VE3.config(state='normal')
    VE4.config(state='normal')
    VE5.config(state='normal')
    VE6.config(state='normal')
    VE7.config(state='normal')
    VE8.config(state='normal')
    VE9.config(state='normal')

    mat_list.config(state='normal')
    contact_entry.config(state='normal')
    niv.config(state='normal')
    return


def controlstateDis():
    LU0.config(state='disabled')
    LU1.config(state='disabled')
    LU2.config(state='disabled')
    LU3.config(state='disabled')
    LU4.config(state='disabled')
    LU5.config(state='disabled')
    LU6.config(state='disabled')
    LU7.config(state='disabled')
    LU8.config(state='disabled')
    LU9.config(state='disabled')

    MA0.config(state='disabled')
    MA1.config(state='disabled')
    MA2.config(state='disabled')
    MA3.config(state='disabled')
    MA4.config(state='disabled')
    MA5.config(state='disabled')
    MA6.config(state='disabled')
    MA7.config(state='disabled')
    MA8.config(state='disabled')
    MA9.config(state='disabled')

    ME0.config(state='disabled')
    ME1.config(state='disabled')
    ME2.config(state='disabled')
    ME3.config(state='disabled')

    JE0.config(state='disabled')
    JE1.config(state='disabled')
    JE2.config(state='disabled')
    JE3.config(state='disabled')
    JE4.config(state='disabled')
    JE5.config(state='disabled')
    JE6.config(state='disabled')
    JE7.config(state='disabled')
    JE8.config(state='disabled')
    JE9.config(state='disabled')

    VE0.config(state='disabled')
    VE1.config(state='disabled')
    VE2.config(state='disabled')
    VE3.config(state='disabled')
    VE4.config(state='disabled')
    VE5.config(state='disabled')
    VE6.config(state='disabled')
    VE7.config(state='disabled')
    VE8.config(state='disabled')
    VE9.config(state='disabled')

    mat_list.config(state='disabled')
    contact_entry.config(state='disabled')
    niv.config(state='disabled')
    return


modebtn1 = Radiobutton(mainframe, text="S'enregistrer en tant que tuteur.", variable=modeout, value=0, command=controlstateEn)
modebtn2 = Radiobutton(mainframe, text="Trouver un tuteur", variable=modeout, value=1, command=controlstateEn)
modebtn3 = Radiobutton(mainframe, text="Se supprimer", variable=modeout, value=2, command=controlstateDis)

# insertion du bouton de validation et de loa progressbar
progbar = ttk.Progressbar(BottomFrame, mode="indeterminate", length=100)

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
modebtn3.grid(column=0, columnspan=1, row=3, sticky='w')

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


def properexit(code):
    showinlog("Exiting with code " + str(code) + "\n")
    quit(code)


def showinlog(message):
    with open("lastestlogs.txt", mode='a') as log:
        log.write(str(datetime.time())+message+str("\n"))
        log.close()
    if "[STDFATAL]" in message:
        return properexit(message)


def popupmaker(title, message, type, textbtnA=None, textbtnB=None):
    errbox = tkinter.Toplevel()
    errbox.title(str(title))
    errlabel = ttk.Label(errbox, text=str(message))
    errlabel.pack()
    def OK():
        errbox.destroy()
        return
    if type == 1:
        errbtn = ttk.Button(errbox, text="OK", command=OK)
        errbtn.pack()
    elif type==2:
        def senderF():
            errbox.destroy()
            return False
        def senderT():
            errbox.destroy()
            return True
        btn1 = ttk.Button(errbox, text="Oui", command=senderT)
        btn2 = ttk.Button(errbox, text='Non', command=senderF)
        btn1.pack()
        btn2.pack()
    elif type == 99:
        def output(outobject):
            return(outobject)
        custombtn1 = ttk.Button(errbox, text=textbtnA, command=output(1))
        custombtn2 = ttk.Button(errbox, text=textbtnB, command=output(0))
        custombtn1.pack()
        custombtn2.pack()


def datastoretuteur(name, grade, disponibilites, matiere, contact):
    showinlog("[STDINFO]: Trying to write in the Database...")
    try:
        with open("tuteurs.csv", mode='a', newline='') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writerow({"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
            TFile.close()
        showinlog("[STDINFO] Successfully done !")
    except FileNotFoundError:
        with open("tuteurs.csv", mode='x') as TFile:
            csvdatabase = csv.DictWriter(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
            csvdatabase.writeheader()
            csvdatabase.writerow(
                {"name": name, "grade": grade, "freehours": disponibilites, "helping": matiere, "contact": contact})
            TFile.close()
        showinlog("[STDINFO]: File tuteurs.csv couldn't be found. A New file name tuteurs.csv has been created.")
    else:
        showinlog("[STDERR]: Couldn't write anything on database !")
    return


def datareformat(datarow,):
    n = 2
    datagroup = []
    while n<len(datarow):
        temp = datarow[n:n+3]
        print(temp)
        datagroup.append(temp)
        n+=7
    print("datagroup",datagroup)
    return datagroup


def reltutoretuteur(nom, niveau, disp, matiere):
    with open('tuteurs.csv', newline='', mode='r') as TFile:
        datastored = csv.DictReader(TFile, fieldnames=["name", "grade", "freehours", "helping", "contact"])
        for row in datastored:
            if matiere == row["helping"]:
                print("Matière OK")
                if int(row["grade"]) <= niveau:
                    print("Classe OK")
                    displist = datareformat(row["freehours"])
                    print(displist)
                    print(disp)
                    for a in range(len(displist)):
                        for b in range(len(disp)):
                            print(displist[a], disp[b])
                            if displist[a] == disp[b]:
                                nomtuteur = row["name"]
                                if 'LU' in disp[b]:
                                    if disp[b] == 'LU0':
                                        tempdisp = 'Lundi de 8h10 à 9h05'
                                    elif disp[b] == 'LU1':
                                        tempdisp = 'Lundi de 9h05 à 10h'
                                    elif disp[b] == 'LU2':
                                        tempdisp = 'Lundi de 10h15 à 11h10'
                                    elif disp[b] == 'LU3':
                                        tempdisp = 'Lundi de 11h10 à 12h05'
                                    elif disp[b] == 'LU4':
                                        tempdisp = 'Lundi de 12h05 à 13h'
                                    elif disp[b] == 'LU5':
                                        tempdisp = 'Lundi de 13h à 13h55'
                                    elif disp[b] == 'LU6':
                                        tempdisp = 'Lundi de 13h55 à 14h50'
                                    elif disp[b] == 'LU7':
                                        tempdisp = 'Lundi de 15h05 à 16h00'
                                    elif disp[b] == 'LU8':
                                        tempdisp = 'Lundi de 16h00 à 17h00'
                                    elif disp[b] == 'LU9':
                                        tempdisp = 'Lundi de 17h00 à 17h55'
                                elif 'MA' in disp[b]:
                                    if disp[b] == 'MA0':
                                        tempdisp = 'Mardi de 8h10 à 9h05'
                                    elif disp[b] == 'MA1':
                                        tempdisp = 'Mardi de 9h05 à 10h'
                                    elif disp[b] == 'MA2':
                                        tempdisp = 'Mardi de 10h15 à 11h10'
                                    elif disp[b] == 'MA3':
                                        tempdisp = 'Mardi de 11h10 à 12h05'
                                    elif disp[b] == 'MA4':
                                        tempdisp = 'Mardi de 12h05 à 13h'
                                    elif disp[b] == 'MA5':
                                        tempdisp = 'Mardi de 13h à 13h55'
                                    elif disp[b] == 'MA6':
                                        tempdisp = 'Mardi de 13h55 à 14h50'
                                    elif disp[b] == 'MA7':
                                        tempdisp = 'Mardi de 15h05 à 16h00'
                                    elif disp[b] == 'MA8':
                                        tempdisp = 'Mardi de 16h00 à 17h00'
                                    elif disp[b] == 'MA9':
                                        tempdisp = 'Mardi de 17h00 à 17h55'
                                elif 'ME' in disp[b]:
                                    if disp[b] == 'ME0':
                                        tempdisp = 'Mercredi de 8h10 à 9h05'
                                    elif disp[b] == 'ME1':
                                        tempdisp = 'Mercredi de 9h05 à 10h'
                                    elif disp[b] == 'ME2':
                                        tempdisp = 'Mercredi de 10h15 à 11h10'
                                    elif disp[b] == 'ME3':
                                        tempdisp = 'Mercredi de 11h10 à 12h05'
                                if 'JE' in disp[b]:
                                    if disp[b] == 'JE0':
                                        tempdisp = 'Jeudi de 8h10 à 9h05'
                                    elif disp[b] == 'Je1':
                                        tempdisp = 'Jeudi de 9h05 à 10h'
                                    elif disp[b] == 'JE2':
                                        tempdisp = 'Jeudi de 10h15 à 11h10'
                                    elif disp[b] == 'JE3':
                                        tempdisp = 'Jeudi de 11h10 à 12h05'
                                    elif disp[b] == 'JE4':
                                        tempdisp = 'Jeudi de 12h05 à 13h'
                                    elif disp[b] == 'JE5':
                                        tempdisp = 'Jeudi de 13h à 13h55'
                                    elif disp[b] == 'JE6':
                                        tempdisp = 'Jeudi de 13h55 à 14h50'
                                    elif disp[b] == 'JE7':
                                        tempdisp = 'Jeudi de 15h05 à 16h00'
                                    elif disp[b] == 'JE8':
                                        tempdisp = 'Jeudi de 16h00 à 17h00'
                                    elif disp[b] == 'JE9':
                                        tempdisp = 'Jeudi de 17h00 à 17h55'
                                elif 'VE' in disp[b]:
                                    if disp[b] == 'VE0':
                                        tempdisp = 'Vendredi de 8h10 à 9h05'
                                    elif disp[b] == 'VE1':
                                        tempdisp = 'Vendredi de 9h05 à 10h'
                                    elif disp[b] == 'VE2':
                                        tempdisp = 'Vendredi de 10h15 à 11h10'
                                    elif disp[b] == 'VE3':
                                        tempdisp = 'Vendredi de 11h10 à 12h05'
                                    elif disp[b] == 'VE4':
                                        tempdisp = 'Vendredi de 12h05 à 13h'
                                    elif disp[b] == 'VE5':
                                        tempdisp = 'Vendredi de 13h à 13h55'
                                    elif disp[b] == 'VE6':
                                        tempdisp = 'Vendredi de 13h55 à 14h50'
                                    elif disp[b] == 'VE7':
                                        tempdisp = 'Vendredi de 15h05 à 16h00'
                                    elif disp[b] == 'VE8':
                                        tempdisp = 'Vendredi de 16h00 à 17h00'
                                    elif disp[b] == 'VE9':
                                        tempdisp = 'Vendredi de 17h00 à 17h55'
                                msg = "Une disponibilité a été trouvée entre "+str(nomtuteur)+" et "+str(nom)+" \n sur le créneau horaire du "+str(tempdisp)+".\n Voulez vous conserver cette disponibilité?"
                                msbox = tkinter.Toplevel()
                                msbox.title("Info: Relation trouvée")
                                mslabel = ttk.Label(msbox, text=msg)
                                mslabel.pack()
                                def conserv():
                                    msbox.destroy()
                                    contact = row["contact"]
                                    if contact.upper() != 'AUCUN' and contact.upper() != 'NONE' and contact.upper() != ' ' and contact.upper != '':
                                        info = "Voici un moyen de contacter le tuteur: " + str(contact)
                                        popupmaker("Information", str(info), 1)
                                        TFile.close()
                                        return
                                    else:
                                        popupmaker("Attention",
                                                         "Aucun moyen de contacter le tuteur n'est entré dans la base de données.",
                                                         99, "Modifier", "OK")
                                        TFile.close()
                                        return
                                def lose():
                                    return msbox.destroy()
                                msbutton = ttk.Button(msbox, text="Oui", command=conserv)
                                msbutton2 = ttk.Button(msbox, text="Non", command=lose)
                                msbutton.pack()
                                msbutton2.pack()

        TFile.close()
    return popupmaker("Information", "Aucune relation possible trouvée.", 1)


def inforegroup(l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, mec0, mec1, mec2, mec3,
                J0, J1, J2, J3, J4, J5, J6, J7, J8, J9, V0, V1, V2, V3, V4, V5, V6, V7, V8, V9):
    lis = [l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, M0, M1, M2, M3, M4, M5, M6, M7, M8, M9, mec0, mec1, mec2, mec3, J0,
           J1, J2, J3, J4, J5, J6, J7, J8, J9, V0, V1, V2, V3, V4, V5, V6, V7, V8, V9]
    showinlog("[STDINFO]: Executing inforegroup function...")
    print(lis)
    disponibs = []
    try:
        for i in range(10):
            if lis[i] == 1:
                disponibs.append('LU'+str(i))
        for j in range(10, 20):
            if lis[j] == 1:
                disponibs.append('MA'+str(j-10))
        for l in range(20, 24):
            if lis[l] == 1:
                disponibs.append('ME'+str(l-20))
        for m in range(24, 34):
            if lis[m] == 1:
                disponibs.append('JE'+str(m-24))
        for n in range(34, 44):
            if lis[n] == 1:
                disponibs.append('VE'+str(n-34))
    except IndexError:
        showinlog("[STDWARN]: Index out of range !")
    showinlog("[STDINFO]: Done !")
    return disponibs

def modessplt(disp):
    showinlog("[STDINFO]: Determining mode to use...")
    print(disp)
    nom = str(name.get())
    print(nom)
    niveau = int(niv.get())
    print(niveau)
    matiere = str(mat_list.get())
    print(matiere)
    contact = str(contact_entry.get())
    print(contact)
    if modeout.get() == 1:
        showinlog("[STDINFO] Initialising reading mode...")
        reltutoretuteur(nom, niveau, disp, matiere)
    elif modeout.get() == 2:
        showinlog("[STDINFO] Initialising deleting mode...")
    else:
        showinlog("[STDINFO] Initialising writing mode...")
        datastoretuteur(nom, niveau, disp, matiere, contact)
    return showinlog("[STDINFO]: Done !")


def reset():
    showinlog("[STDINFO]: Reseting users choices...")
    lu0.set(0)
    lu1.set(0)
    lu3.set(0)
    lu4.set(0)
    lu5.set(0)
    lu6.set(0)
    lu7.set(0)
    lu8.set(0)
    lu9.set(0)

    ma0.set(0)
    ma1.set(0)
    ma2.set(0)
    ma3.set(0)
    ma4.set(0)
    ma5.set(0)
    ma6.set(0)
    ma7.set(0)
    ma8.set(0)
    ma9.set(0)

    me0.set(0)
    me1.set(0)
    me2.set(0)
    me3.set(0)

    je0.set(0)
    je1.set(0)
    je2.set(0)
    je3.set(0)
    je4.set(0)
    je5.set(0)
    je6.set(0)
    je7.set(0)
    je8.set(0)
    je9.set(0)

    ve0.set(0)
    ve1.set(0)
    ve2.set(0)
    ve3.set(0)
    ve4.set(0)
    ve5.set(0)
    ve6.set(0)
    ve7.set(0)
    ve8.set(0)
    ve9.set(0)
    name_entry.delete(0, "end")
    contact_entry.delete(0, "end")
    niv.set(0)
    mat_list.delete(0, "end")
    return showinlog("[STDINFO]: Done !")


def launch():
    progbar.start()
    if str(name_entry.get()) == '' or str(mat_list.get()) == '':
        showinlog("[STDWARN]: Missing data to start other processes !")
        popupmaker('Erreur de saisie', "Erreur: Une ou plusieurs entrée textuelle obligatoires sont vides.", 1)
        return progbar.stop()
    showinlog("[STDINFO]: Executing program...")
    disponibilites = inforegroup(lu0.get(), lu1.get(), lu2.get(), lu3.get(), lu4.get(), lu5.get(), lu6.get(), lu7.get(), lu8.get(), lu9.get(), ma0.get(), ma1.get(), ma2.get(), ma3.get(), ma4.get(), ma5.get(), ma6.get(),
                                 ma7.get(), ma8.get(), ma9.get(), me0.get(), me1.get(), me2.get(), me3.get(), je0.get(), je1.get(), je2.get(), je3.get(), je4.get(), je5.get(), je6.get(), je7.get(), je8.get(), je9.get(),
                                 ve0.get(), ve1.get(), ve2.get(), ve3.get(), ve4.get(), ve5.get(), ve6.get(), ve7.get(), ve8.get(), ve9.get())
    if len(disponibilites) == 0:
        showinlog("[STDWARN]: Missing data to start other processes !")
        popupmaker('Erreur de saisie', "Erreur: Aucun créneau horaire de disponibilité saisi.", 1)
        return progbar.stop()
    modessplt(disponibilites)
    progbar.stop()
    reset()
    showinlog("[STDINFO]: Done !")


name_label.grid(sticky='sw', column=0, row=3)
name_entry.grid(sticky='sw', column=0, row=4)
label_blank6.grid(sticky='sw', column=1, row=3)
contact_label.grid(sticky='sw', column=2, row=3)
contact_entry.grid(sticky='sw', column=2, row=4)
label_blank7.grid(sticky='sw', column=3, row=3)
mat_label.grid(sticky='sw', column=4, row=3)
mat_list.grid(sticky='sw', column=4, row=4)
label_blank8.grid(sticky='sw', column=5, row=3)
validation = ttk.Button(BottomFrame, text="Valider", command=launch)
label_blank9.grid(sticky='sw', column=7, row=4)
progbar.grid(sticky='se', column=8, row=4)


#Initialisation des derniers composants
validation.grid(sticky='sw', column=6, row=4)

# activation des frames:
mainframe.grid(sticky='n')
EDTFrame.grid(sticky='n', column=0, columnspan=6, row=4, rowspan=12)
BottomFrame.grid(sticky='s')

# activation de l'IUG
interface.mainloop()