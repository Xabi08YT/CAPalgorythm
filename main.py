import pandas
import os
import tkinter
from tkinter import Button, Checkbutton, Frame, Radiobutton
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
from datetime import *
import csv
import unidecode
from CoreProxy import *


newLogs = False
isDB1loaded = False
isDB2loaded = False
isDB3loaded = True
isConfigLoaded = False

##Fonction d'Ecriture d'informations de debuggage
def printInLogs(objet, categorie, forceshowing = False):
    CoreLibs.utils.printInLogs(objet, categorie, forceshowing = False)
    return



################################################################################################################################
##                                          Initialisation du programme                                                       ##
################################################################################################################################
def init():
    global tuteursDB,relDB, feedback, config, isConfigLoaded, isDB1loaded, isDB2loaded, isDB3loaded, newLogs
    CoreLibs.utils.init()
    tuteursDB,relDB, feedback, config, isConfigLoaded, isDB1loaded, isDB2loaded, isDB3loaded, newLogs = CoreLibs.utils.getVars()
    return


##Fonction de création de msgbox
def newmsgbox(title, message, type, textbtnA=None, textbtnB=None):
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

##Fonction de réinitialisation des bases de donnees
def resetDB():
    global isDB1loaded; isDB2loaded, isDB3loaded
    printInLogs("Requesting User...", 0)
    msgbox = tkinter.Toplevel()
    msgbox.title("Avertissement")
    msg = ttk.Label(msgbox, text = "Toutes les bases de données seront réinitialisées. Cette action est irréversible. Souhaitez-vous continuer ?")
    def YES():
        msgbox.destroy()
        printInLogs("Début de la réinitialisation des bases de données...")
        CoreLibs.basicDBCtrl.resetDB()
        printInLogs("Bases de données supprimées avec succès. Début d'une nouvelle initialisation...",0)
        init()
        newmsgbox("Information","Bases de données réinitialisées avec succès.", 1)
        printInLogs("Réinitialisation terminée.", 0)
        return
    def NO():
        msgbox.destroy()
        printInLogs("Réinitialisation annulée.", 0)
        return
    yesbutton = ttk.Button(msgbox, text = "Oui", command = YES)
    nobutton = ttk.Button(msgbox, text = "Non", command = NO)
    msg.grid(column = 0, row = 0)
    yesbutton.grid(column = 3, row = 1)
    nobutton.grid(column = 4, row = 1)
    return


##Fonction qui regroupe les informations obtenues
def regroupInfos():
    lis = [lu0.get(),lu1.get(),lu2.get(),lu3.get(), lu4.get(), lu5.get(), lu6.get(), lu7.get(),lu8.get(),lu9.get(), ma0.get(),ma1.get(),ma2.get(),ma3.get(),ma4.get(),ma5.get(),ma6.get(),ma7.get(),ma8.get(),ma9.get(),me0.get(),me1.get(),me2.get(),me3.get(),
        je0.get(),je1.get(),je2.get(),je3.get(),je4.get(),je5.get(),je6.get(),je7.get(),je8.get(),je9.get(),ve0.get(),ve1.get(),ve2.get(),ve3.get(),ve4.get(),ve5.get(),ve6.get(),ve7.get(), ve8.get(), ve9.get()]
    printInLogs("Creation d'une table contenant les disponibilites...", 0)
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
        printInLogs("L'index est hors de portée !",1)
    printInLogs("Opération terminée.",0)
    return disponibs


##Fonction d'actualisation des bases de données
def actualiserDB():
    global tuteursDB, relDB, feedback
    tuteursDB, relDB, feedback = CoreLibs.utils.actualiserDB()
    return


##Fonction d'actualisation de la configuration
def actualiserConfig():
    global config
    config = CoreLibs.utils.actualiserConfig()
    return


##Fonction de modification de la configuration
def modifConfig(logsOpt,feedbackOpt, RelDB):
    printInLogs("Modification de la configuration suivant les choix de l'utilisateur...",0, True)
    global config
    config = actualiserConfig()
    return


##Fonction permettant l'appel du menu de configuration
def afficherConfigMenu():
    global config, enableFeedback, enableLogs, enableRelDB
    def appliquer():
        optMenu.destroy()
        modifConfig(enableLogs.get(), enableFeedback.get(),enableRelDB.get())
        return
    def annuler():
        optMenu.destroy()
        return
    optMenu = tkinter.Toplevel()
    optMenu.title("Menu des Options")
    optFrame = Frame(optMenu)
    optLabel = tkinter.Label(optFrame, text = "Bienvenue dans le menu de configuration du programme.\n Vous sélectionnerez ici certains comportements du programme.")
    blanklabel = tkinter.Label(optFrame,text="              ")
    enableLogs.set(str(config["enableLogs"]))
    enableFeedback.set(str(config["enableFeedback"]))
    enableRelDB.set(str(config["enableRelDB"]))
    logOptnLabel = tkinter.Label(optFrame,text="Activer les journaux de débuggage:")
    feedbackOptnLabel = tkinter.Label(optFrame,text="Activer la base de données contenant les avis concernant\n les relations effectuées (non géré pour le moment):")
    relationOptnLabel = tkinter.Label(optFrame,text="Activer le gestionnaire de relations entre tuteurs et tutorés (WIP)")
    enableLogsCheck = Checkbutton(optFrame,onvalue=True,offvalue=False,variable=enableLogs)
    enableFeedbackCheck = Checkbutton(optFrame,onvalue=True,offvalue=False,variable=enableFeedback)
    enableRelDBCheck = Checkbutton(optFrame,onvalue=True,offvalue=False,variable=enableRelDB)
    logOptnLabel.grid(column=0, row=1, columnspan=3)
    feedbackOptnLabel.grid(column=0, row=2, columnspan= 5,sticky="w")
    relationOptnLabel.grid(column=0, row=3,columnspan=5,sticky='w')
    enableLogsCheck.grid(column=6, row = 1)
    enableFeedbackCheck.grid(column=6, row = 2)
    enableRelDBCheck.grid(column=6, row = 3)
    blanklabel.grid(column=5,row = 1)
    optLabel.grid(column = 0, columnspan = 7, row=0)
    optAppliquerBtn = Button(optFrame, text = "Appliquer", command=appliquer)
    optAnnulerBtn = Button(optFrame, text="Annuler", command=annuler)
    optAppliquerBtn.grid(column = 5, row = 4)
    optAnnulerBtn.grid(column = 6, row= 4)
    optFrame.grid(column=0, row=0)
    return


##Fonction de restauration de la configuration par défaut
def configDefaut():
    printInLogs("Restauration de la configuration par défaut...", 0, True)
    os.remove(path="config.csv")
    actualiserConfig()
    return


##Fonction qui retire les caractères spéciaux afin d'éviter la création du crash loop
def unicode_serialize(texts:list):
    texts = CoreLibs.utils.unicode_serialize(texts)
    return texts


##Fonction d'ajout de tuteurs dans la base de données
def ajouterTuteur(nom, pnm, niveau, dispos, matiere, contact):
    newRow = {'nom': nom, 'prenom': pnm,'niveau': niveau, 'disponibilites': dispos,'matiere': matiere, 'contact': contact}
    if estDansBase(newRow):
        newmsgbox("Erreur","Ces informations ont déjà été entrées dans la base de données",1)
        return
    with open(file = "tuteurs.csv", mode = 'a+',newline="") as database:
        windb = csv.DictWriter(database, ['nom', 'prenom','niveau','disponibilites','matiere','contact'])
        windb.writerow(newRow)
        database.close()
    actualiserDB()
    return


##Fonction qui permet de trouver un tuteur
def trouverTuteur(nom, prn, niveau, matiere, dispos):
    msgout, rels, treatmentType = CoreLibs.tuteurs.trouverTuteur(nom, prn, niveau, matiere, dispos)
    if treatmentType == None:
        newmsgbox(msgout[0], msgout[1], msgout[2])
    return


##Fonction permettant de supprimer un tuteur de la base de données
def supprimerTuteur(nom, prn, matiere):
    print("suppression...") 
    out = CoreLibs.tuteurs.supprimerTuteur(nom, prn, matiere)
    if out is not None:
        newmsgbox(out[0],out[1],out[2])
    actualiserDB()
    return


def FusionnerDB():
    target = filedialog.askopenfilename(initialdir =  "/",title = "Select file",filetypes = (("CSV", "*.csv "),("all files", "*.*")))
    out = CoreLibs.tuteurs.FusionnerDB(target)
    if out is not None:
        newmsgbox(out)
    return


#Vérification contre les conflits
def estDansBase(row):
    global tuteursDB
    estDansDB = CoreLibs.tuteurs.estDansBase(tuteursDB, row)
    return estDansDB


##Fonction permettant de déterminer le mode de fonctionnement
def modessplt(disp):
    printInLogs("Determining mode to use...", 0)
    nom = str(name.get())
    print(nom)
    pren = str(prenom.get())
    print(pren)
    niveau = int(niv.get())
    print(niveau)
    print(disp)
    matiere = str(mat_list.get())
    print(matiere)
    contact = str(contact_entry.get())
    print(contact)
    serialized = unicode_serialize([nom,pren,contact])
    if modeout.get() == 1:
        printInLogs("Initialisation du mode lecture...", 0)
        trouverTuteur(serialized[0],serialized[1], niveau, matiere, disp)
    elif modeout.get() == 0:
        printInLogs("Initialisation du mode d'écriture...", 0)
        ajouterTuteur(serialized[0], serialized[1], niveau, disp, matiere, serialized[2])
    else:
        printInLogs("Initialisation du mode de suppression...", 0)
        supprimerTuteur(serialized[0], serialized[1], matiere)
    return printInLogs("Opération terminée.", 0)


##Fonction de réinitialisation des champs
def reset():
    printInLogs("Réinitialisation des champs de saisies...", 0)
    lu0.set(0)
    lu1.set(0)
    lu2.set(0)
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
    prenom_entry.delete(0,'end')
    contact_entry.delete(0, "end")
    niv.set(0)
    mat_list.delete(0, "end")
    return printInLogs("Opération terminée.", 0)



##Foction de validation
def Valider():
    progbar.start()
    dispos = regroupInfos()
    if str(name_entry.get()) == '' or str(prenom_entry.get()) == '' or str(mat_list.get()) == '' or len(dispos) == 0 and modeout.get() != 2:
        printInLogs("Données manquantes pour le lancement de processus...",1)
        newmsgbox('Erreur de saisie', "Erreur: Une ou plusieurs entrée textuelle obligatoires sont vides.", 1)
        return progbar.stop()
    modessplt(dispos)
    reset()
    progbar.stop()
    return


##Création de l'IUG
# initialisation de l'interface graphique
interface = tkinter.Tk()
interface.title("Interface base de données CAPS")
interface.geometry("1500x720")
interface.minsize(1500, 720)
try:
    interface.iconphoto(True, tkinter.PhotoImage(file='logo.png'))
except Exception:
    pass

enableLogs = tkinter.BooleanVar()
enableFeedback = tkinter.BooleanVar()
enableRelDB = tkinter.BooleanVar()

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
prenom = tkinter.StringVar()
cont = tkinter.StringVar()
mat = tkinter.StringVar()
nivvar = tkinter.IntVar()
nivvar.set(0)
Listematiere = ["Allemand" ,"Histoire-Geographie", "Education Morale et Civique", "Espagnol",  "HGGSP", "Enseignement-scientifique SVT","Enseignement scientifique Physique","Francais", "Anglais","SES", "HLP",
"Philosophie", "Litt. Anglaise", "Mathematiques" ,"Mathématiques tronc-commun (TC)","Musique","NSI/SNT", "Physique Spe", "SVT Spe"]


# initialisation des frames
mainframe = ttk.Frame(interface)
menuframe = ttk.Frame(interface)
TopFrame = ttk.Frame(interface)
EDTFrame = ttk.Frame(interface)
BottomFrame = ttk.Frame(interface)
OptnFrame = ttk.Frame(interface)

# ajout du premier texte
label_mode = ttk.Label(TopFrame, text="Veuillez choisir le mode de fonctionnement de l'application:")

# ajout du deuxième texte
label_level = ttk.Label(TopFrame, text="Veuillez sélectionner le niveau (0 pour terminale, 1 pour première, 2 pour seconde) de la personne concernée.")

# Insertion de la barre permettant de choisir le niveau de la personne concernée
niv = tkinter.Scale(TopFrame, from_=0, to=2, orient='horizontal', variable=nivvar)

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
name_label = tkinter.Label(BottomFrame, text="Entrez le nom de la personne:")
name_entry = tkinter.Entry(BottomFrame, width=30, textvariable=name)
prenom_label =  tkinter.Label(BottomFrame, text = "Entrez le prenom de la personne: ")
prenom_entry = tkinter.Entry(BottomFrame, width=30, textvariable=prenom)
contact_label = tkinter.Label(BottomFrame, text="Entrez un moyen de contacter la personne: (factultatif)")
contact_entry = tkinter.Entry(BottomFrame, width=30, textvariable=cont)
mat_label = tkinter.Label(BottomFrame, text="Sélectionnez la matière de la personne:")
mat_list = ttk.Combobox(BottomFrame, values=Listematiere, width=30, textvariable=mat)


# insertion des elements la barre d'actions rapides
resetDBBTN = Button(OptnFrame, text="Réinitialiser les bases de données" , command=resetDB)
optnBTN = Button(OptnFrame, text="Options du logiciel", command=afficherConfigMenu)
resetConfigBtn = Button(OptnFrame, text="Rétablir la configuration par défaut", command=configDefaut)
fusionDBBtn = Button(OptnFrame,text="Fusionner des base de données", command=FusionnerDB)

# Menus d'options
fileMenu = ""

# Insertions des boutons de radio
modebtn1 = Radiobutton(TopFrame, text="S'enregistrer en tant que tuteur.", variable=modeout, value=0)
modebtn2 = Radiobutton(TopFrame, text="Trouver un tuteur", variable=modeout, value=1)
modebtn3 = Radiobutton(TopFrame, text="Supprimer un tuteur", variable=modeout, value=2)

# insertion du bouton de validation et de la progressbar
progbar = ttk.Progressbar(BottomFrame, mode="indeterminate", length=100)

# Mise en page
label_blank = tkinter.Label(TopFrame, text="        ")
label_blank1 = tkinter.Label(TopFrame, text="        ")
label_blank2 = tkinter.Label(TopFrame, text="        ")
label_blank3 = tkinter.Label(mainframe, text="        ")
label_blank4 = tkinter.Label(BottomFrame, text="        ")
label_blank5 = tkinter.Label(BottomFrame, text="        ")
label_blank6 = tkinter.Label(BottomFrame, text="            ")
label_blank7 = tkinter.Label(BottomFrame, text="            ")
label_blank8 = tkinter.Label(BottomFrame, text="            ")
label_blank9 = tkinter.Label(BottomFrame, text="            ")
label_blank10 = tkinter.Label(mainframe, text="                 ")
label_blank11 = tkinter.Label(mainframe, text="                 ")
label_blank12 = tkinter.Label(mainframe, text="                 ")
label_blank13 = tkinter.Label(BottomFrame, text="                 ")

label_mode.grid(column=0, columnspan=1, row=0, sticky='e')
modebtn1.grid(column=0, columnspan=1, row=1, sticky='w')
modebtn2.grid(column=0, columnspan=1, row=2, sticky='w')
modebtn3.grid(column=0, columnspan=1, row=3, sticky='w')

label_blank.grid(column=4, row=0, columnspan=1)
label_blank1.grid(column=5, row=0, columnspan=1)
label_blank2.grid(column=6, row=0, columnspan=1)

label_level.grid(column=10, row=0, columnspan=1, sticky="w")
niv.grid(column=10, row=1, sticky = "w")

label_blank3.grid(columnspan=10, column=0, row=3)
label_blank10.grid(column = 10, row=0)
label_blank11.grid(column = 11, row=0)
label_blank12.grid(column = 12, row=0)

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
prenom_label.grid(sticky = 'sw', column = 2, row = 3)
prenom_entry.grid(sticky = 'sw', column = 2, row = 4)
label_blank13.grid(sticky = 'sw', column = 3, row = 3)
contact_label.grid(sticky='sw', column=4, row=3)
contact_entry.grid(sticky='sw', column=4, row=4)
label_blank7.grid(sticky='sw', column=5, row=3)
mat_label.grid(sticky='sw', column=6, row=3)
mat_list.grid(sticky='sw', column=6, row=4)
label_blank8.grid(sticky='sw', column=7, row=3)
validation = ttk.Button(BottomFrame, text="Valider", command=Valider)
label_blank9.grid(sticky='sw', column=9, row=4)
progbar.grid(sticky='se', column=10, row=4)
resetDBBTN.grid(sticky='s', column=2, row=4)
optnBTN.grid(sticky='s', column=2, row=5)
resetConfigBtn.grid(sticky='s', column=2, row=6)
fusionDBBtn.grid(sticky='s',column=2,row=7)


#Initialisation des derniers composants
validation.grid(sticky='sw', column=8, row=4)

# activation des frames:
mainframe.grid(sticky ='n')
TopFrame.grid(column = 0, row = 0, columnspan=5)
EDTFrame.grid(sticky ='n', column=0, columnspan=6, row=4, rowspan=12)
BottomFrame.grid(sticky ='s')
OptnFrame.grid(column = 10, row = 0)

#Appel de l'init du programme
init()

#Lancement de l'IUG
interface.mainloop()
