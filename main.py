import os
import tkinter
from tkinter import Button, Checkbutton, Frame, Radiobutton
from tkinter import filedialog
import tkinter.ttk as ttk
from datetime import *
from CoreProxy import *


newLogs = False
isDB1loaded = False
isDB2loaded = False
isDB3loaded = False
isConfigLoaded = False
selectedRelID = None
creneaux = CoreLibs.utils.creneaux


##Fonction d'Ecriture d'informations de debuggage
def printInLogs(objet, categorie, forceshowing = False):
    CoreLibs.utils.printInLogs(objet, categorie, forceshowing)
    return



################################################################################################################################
##                                          Initialisation du programme                                                       ##
################################################################################################################################
def init():
    global tuteursDB,relDB, feedback, config, isConfigLoaded, isDB1loaded, isDB2loaded, isDB3loaded, newLogs
    CoreLibs.utils.init()
    tuteursDB,relDB, feedback, config, isConfigLoaded, isDB1loaded, isDB2loaded, isDB3loaded, newLogs = CoreLibs.utils.getVars()
    appliquerConfig()
    if config["enableRelDB"]:
        CoreLibs.relations.buildIDList()
    if config["enableFeedback"]:
        CoreLibs.feedback.buildIDList()
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


##Application de la configuration
def appliquerConfig():
    if not config["enableRelDB"]:
        tabs.tab(1, state = "disabled")
    else:
        tabs.tab(1, state = "normal")
    if not config["enableFeedback"]:
        tabs.tab(2, state = "disabled")
    else:
        tabs.tab(2, state = "normal")
    actualiserDB()


##Fonction d'actualisation des bases de données
def actualiserDB():
    global tuteursDB, relDB, feedback
    tuteursDB, relDB, feedback = CoreLibs.utils.actualiserDB()
    return


##Fonction d'actualisation de la configuration
def actualiserConfig():
    global config
    config = CoreLibs.utils.actualiserConfig()
    appliquerConfig()
    return


##Fonction de modification de la configuration
def modifConfig(logsOpt,feedbackOpt, RelDB):
    printInLogs("Modification de la configuration suivant les choix de l'utilisateur...",0, True)
    global config
    CoreLibs.basicDBCtrl.editConfig(logsOpt,feedbackOpt, RelDB)
    actualiserConfig()
    print(config)
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
    feedbackOptnLabel = tkinter.Label(optFrame,text="Activer la base de données contenant les avis concernant\n les relations effectuées (WIP):")
    relationOptnLabel = tkinter.Label(optFrame,text="Activer le gestionnaire de relations entre tuteurs et tutorés")
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
    CoreLibs.tuteurs.ajouter(newRow)
    actualiserDB()
    return


##Fonction qui permet de trouver un tuteur
def trouverTuteur(nom, prn, niveau, matiere, dispos):
    msgout, rels, treatmentType = CoreLibs.tuteurs.trouverTuteur(nom, prn, niveau, matiere, dispos)
    if treatmentType == None:
        newmsgbox(msgout[0], msgout[1], msgout[2])
    elif treatmentType == 1:
        def ajouter():
            resultWindow.destroy()
            CoreLibs.relations.addRel(rels[selData[0]])
            actualiserDB()
            return
        
        selData = None
        
        def currentchoice(a):
            curSel = resultTree.focus()
            curselData = resultTree.item(curSel)
            if curselData["values"] == "" or config["enableRelDB"] == False:
                addBTN["state"] = "disabled"
            else:
                addBTN["state"] = "enabled"
            nonlocal selData
            selData = curselData["values"]
            return
        
        def close():
            resultWindow.destroy()
            return

        resultWindow = tkinter.Toplevel(interface)
        resultWindow.title = "Résultats de la recherche"
        resFrame = ttk.Frame(resultWindow)
        relscroll = ttk.Scrollbar(resFrame)
        resultTree = ttk.Treeview(resFrame, columns=("c1","c2","c3", "c4", "c5", "c6","c7"), show='headings', height=25, yscrollcommand=relscroll.set)
        resultTree.column("# 1", anchor=tkinter.CENTER,  width = 10)
        resultTree.heading("# 1", text="ID")
        resultTree.column("# 2", anchor=tkinter.CENTER,  width = 200)
        resultTree.heading("# 2", text="Nom tuteur")
        resultTree.column("# 3", anchor=tkinter.CENTER,  width = 200)
        resultTree.heading("# 3", text="Prenom tuteur")
        resultTree.column("# 4", anchor=tkinter.CENTER,  width = 200)
        resultTree.heading("# 4", text="Nom tutore")
        resultTree.column("# 5", anchor=tkinter.CENTER,  width = 200)
        resultTree.heading("# 5", text="Prenom tutore")
        resultTree.column("# 6", anchor=tkinter.CENTER,  width = 90)
        resultTree.heading("# 6", text="Matiere")
        resultTree.column("# 7", anchor=tkinter.CENTER,  width = 150)
        resultTree.heading("# 7", text="Horaire")
        resultTree.bind('<Button-1>', currentchoice)
        resultTree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        relscroll.config(command=resultTree.yview)
        relscroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        addBTN = ttk.Button(resultWindow, text="Ajouter la relation à la base de données", command=ajouter)
        closeBTN = ttk.Button(resultWindow, text="Fermer", command=close)
        addBTN.grid(column=1, row=0)
        closeBTN.grid(column=1, row=1)
        resFrame.grid(column=0, row=0, rowspan=25)
        for e,i in zip(rels, range(len(rels))):
            resultTree.insert('', 'end', text=str(i), values=(i,e["tuteur"][0],e["tuteur"][1],e["tutore"][0],e["tutore"][1],e["matiere"],creneaux[e["horaire"]]))
    return


##Fonction permettant de supprimer un tuteur de la base de données
def supprimerTuteur(nom, prn, matiere):
    print("suppression...") 
    out = CoreLibs.tuteurs.supprimerTuteur(nom, prn, matiere)
    if out is not None:
        newmsgbox(out[0],out[1],out[2])
    actualiserDB()
    return


def FusionnerDBTuteurs():
    target = filedialog.askopenfilename(initialdir =  "/",title = "Select file",filetypes = (("CSV", "*.csv "),("all files", "*.*")))
    out = CoreLibs.tuteurs.FusionnerDB(target)
    if out is not None:
        newmsgbox("Erreur",out,1)
    return


def FusionnerDBRelations():
    target = filedialog.askopenfilename(initialdir =  "/",title = "Select file",filetypes = (("CSV", "*.csv "),("all files", "*.*")))
    out = CoreLibs.relations.FusionnerDB(target)
    if out is not None:
        newmsgbox("Erreur",out,1)
    return 


def FusionnerDBFeedback():
    target = filedialog.askopenfilename(initialdir =  "/",title = "Select file",filetypes = (("CSV", "*.csv "),("all files", "*.*")))
    out = CoreLibs.feedback.FusionnerDB(target)
    if out is not None:
        newmsgbox("Erreur",out,1)
    return


#Fonction qui affiche les relations existantes
def refreshRelPrint():
    actualiserDB()
    rmBTN["state"] = "disabled"
    feedbackBTN["state"] = "disabled"
    endRelBTN["state"] = "disabled"
    for child in principalView.get_children():
        principalView.delete(child)
    if len(relDB) == 0:
        principalView.insert('', 'end', text="1", values=("Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée."))
        return
    for i in range(len(relDB)):
        tuteurInfos = relDB.loc[i,"tuteur"].split(",")
        tutoreInfos = relDB.loc[i,"tutore"].split(",")
        for j in range(2):
            tuteurInfos[j] = tuteurInfos[j].replace("'","")
            tuteurInfos[j] = tuteurInfos[j].replace("(","")
            tuteurInfos[j] = tuteurInfos[j].replace(")","")
            tutoreInfos[j] = tutoreInfos[j].replace("'","")
            tutoreInfos[j] = tutoreInfos[j].replace("(","")
            tutoreInfos[j] = tutoreInfos[j].replace(")","")
        principalView.insert('', 'end', text=str(i), values=(relDB.loc[i,"id"],tuteurInfos[0], tuteurInfos[1],tutoreInfos[0],tutoreInfos[1],relDB.loc[i,"matiere"], CoreLibs.utils.creneaux[relDB.loc[i,"horaire"]]))
    return


def refreshFeedbackPrint():
    actualiserDB()
    rmBTNFeedback["state"] = "disabled"
    editBTNFeedback["state"] = "disabled"
    for child in feedview.get_children():
        feedview.delete(child)
    if len(feedback) == 0:
        feedview.insert('', 'end', text="1", values=("Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée.","Aucune Donnée."))
        return
    for i in range(len(feedback)):
        tuteurInfos = feedback.loc[i,"tuteur"].split(",")
        tutoreInfos = feedback.loc[i,"tutore"].split(",")
        for j in range(2):
            tuteurInfos[j] = tuteurInfos[j].replace("'","")
            tuteurInfos[j] = tuteurInfos[j].replace("(","")
            tuteurInfos[j] = tuteurInfos[j].replace(")","")
            tutoreInfos[j] = tutoreInfos[j].replace("'","")
            tutoreInfos[j] = tutoreInfos[j].replace("(","")
            tutoreInfos[j] = tutoreInfos[j].replace(")","")
        feedview.insert('', 'end', text=str(i), values=(feedback.loc[i,"feedbackid"],tuteurInfos[0], tuteurInfos[1],tutoreInfos[0],tutoreInfos[1],feedback.loc[i,"caractere"],feedback.loc[i,"matiere"], feedback.loc[i,"efficacite"],feedback.loc[i, "idrelation"], feedback.loc[i,"commentaires"]))
    return


#Fonction qui récupère l'id de la selection
def selectItemRel(a):
    global selectedRelID
    curItem = principalView.focus()
    selectedRelID = principalView.item(curItem)
    if selectedRelID["values"] == '':
        newmsgbox("Information","Votre selection n'a pas été prise en compte. Veuillez re-sélectioner l'élément.", 1)
        rmBTN["state"] = "disabled"
        feedbackBTN["state"] = "disabled"
        endRelBTN["state"] = "disabled"
        return
    selectedRelID = selectedRelID["values"][0]
    if selectedRelID == "Aucune Donnée.":
        rmBTN["state"] = "disabled"
        feedbackBTN["state"] = "disabled"
        endRelBTN["state"] = "disabled"
    else:
        rmBTN["state"] = "enabled"
        feedbackBTN["state"] = "enabled"
        endRelBTN["state"] = "enabled"
    return


#Fonction qui récupère l'id de la selection
def selectItemFeedback(a):
    global selectedFeedbackID
    curItem = feedview.focus()
    selectedFeedbackID = feedview.item(curItem)
    if selectedFeedbackID["values"] == '':
        newmsgbox("Information","Votre selection n'a pas été prise en compte. Veuillez re-sélectioner l'élément.", 1)
        rmBTNFeedback["state"] = "disabled"
        editBTNFeedback["state"] = "disabled"
        return
    selectedFeedbackID = selectedFeedbackID["values"][0]
    if selectedFeedbackID == "Aucune Donnée.":
        rmBTNFeedback["state"] = "disabled"
        editBTNFeedback["state"] = "disabled"
    else:
        rmBTNFeedback["state"] = "enabled"
        editBTNFeedback["state"] = "enabled"
    return


#Suppression de relation
def delRel():
    out = CoreLibs.relations.rmRel(selectedRelID)
    if out != None:
        newmsgbox("Information",out,1)
    actualiserDB()
    refreshRelPrint()
    return


#Suppression de relation
def delFeedback():
    out = CoreLibs.feedback.removeFeedbackByID(selectedFeedbackID)
    if out != None:
        newmsgbox("Information",out,1)
    actualiserDB()
    refreshFeedbackPrint()
    return


##Fonction pour obtenir le feedback de l'utilisateur
def getFeedbackFromUser():
    out = None
    caractere = tkinter.StringVar()
    efficacite = tkinter.StringVar()
    commentaire = tkinter.StringVar()
    def Confirmer():
        nonlocal out
        try:
            out = (int(caractere.get()), int(efficacite.get()), commentaire.get())
            feedbackprompt.destroy()
        except ValueError:
            newmsgbox("Plusieurs condition non respectée.", "Conditions non respectées, verifiez les informations entrées.",1)
        return
    
    def Annuler():
        feedbackprompt.destroy()
        return
    
    feedbackprompt = tkinter.Toplevel(interface)
    feedbackprompt.title = "Entrée d'avis"
    caractNote = ttk.Label(feedbackprompt, text="Entrez une note /5 concernant la bonne entente dans le groupe:")
    efficaciteNote = ttk.Label(feedbackprompt, text="Entrez une note /5 d'efficacite du binome:")
    commentaireLabel = ttk.Label(feedbackprompt, text="Entrez un commentaire plus détaillé ici (facultatif):")
    caractEntree = ttk.Entry(feedbackprompt, textvariable=caractere)
    efficacitEntree = ttk.Entry(feedbackprompt, textvariable=efficacite)
    commentaireEntree = ttk.Entry(feedbackprompt, textvariable=commentaire, width=200)
    confirmBTN = ttk.Button(feedbackprompt,text="Confirmer", command=Confirmer)
    annulerBTN = ttk.Button(feedbackprompt, text="Annuler", command=Annuler)
    caractNote.grid(column=0, row=0, columnspan=5)
    efficaciteNote.grid(column=7, row=0, columnspan=5)
    commentaireLabel.grid(column=0, row=7, columnspan=12)
    caractEntree.grid(column=0, row=1, rowspan=5, columnspan=5)
    efficacitEntree.grid(column=7, row=1, rowspan=5, columnspan=5)
    commentaireEntree.grid(column=0, row=8, rowspan=5, columnspan=12)
    confirmBTN.grid(column=5, row=16)
    annulerBTN.grid(column=7, row=16)
    feedbackprompt.wait_window()
    return out


##Modification d'avis par la sélection d'une relation
def modifyFeedbackByRel():
    usrEntry = getFeedbackFromUser()
    oldData = CoreLibs.feedback.getFeedbackIdByRelID(selectedRelID)
    if usrEntry == None:
        return
    try:
        if oldData == None:
            CoreLibs.feedback.ajouterFeedback(usrEntry[1],usrEntry[0], selectedRelID, True, usrEntry[2])
            return
    except ValueError: 
        pass
    CoreLibs.feedback.replaceFeedback(oldData["feedbackid"], usrEntry[1],usrEntry[0],selectedRelID,True,usrEntry[2])
    return


##Modification d'avis par la sélection d'un avis
def modifyFeedbackByFeedback():
    usrEntry = getFeedbackFromUser()
    oldData = CoreLibs.feedback.getFeedbackByID(selectedFeedbackID)
    if usrEntry == None:
        return
    try:
        if oldData == None:
            return
    except ValueError:
        pass
    else:
        oldData = oldData[1]
        CoreLibs.feedback.replaceFeedback(oldData["feedbackid"],usrEntry[1],usrEntry[0],oldData["idrelation"],True,usrEntry[2], oldData["tuteur"],oldData["tutore"],oldData["matiere"])
    return


##fonction appellée lors de la fin d'une relation
def finRelation():
    usrEntry = getFeedbackFromUser()
    oldData = CoreLibs.feedback.getFeedbackIdByRelID(selectedRelID)
    print(str(oldData))
    if usrEntry == None:
        return
    try:
        if oldData == None:
            out = CoreLibs.feedback.ajouterFeedback(usrEntry[1],usrEntry[0], selectedRelID, False, usrEntry[2])
    except ValueError:
        out = CoreLibs.feedback.replaceFeedback(oldData["feedbackid"], usrEntry[1],usrEntry[0],selectedRelID,False,usrEntry[2])
    delRel()
    return


#Fonction anti-doublons
def estDansBase(row):
    global tuteursDB
    estDansDB = CoreLibs.tuteurs.estDansBase(row)
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
interface.title("Utilitaire CAPS")
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

# Menus d'options
menuBar = tkinter.Menu(interface)
interface.config(menu=menuBar)
fileMenu = tkinter.Menu(menuBar,tearoff=0)
settingsMenu = tkinter.Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Fichier",menu=fileMenu)
menuBar.add_cascade(label="Options",menu=settingsMenu)

# Ajout d'options
fileMenu.add_command(label = "Actualiser les bases de données", command=actualiserDB)
fileMenu.add_command(label = "Réinitialiser les bases de données", command=resetDB)
fileMenu.add_separator()
fileMenu.add_command(label = "Fusionner deux bases de données de tuteurs", command=FusionnerDBTuteurs)
fileMenu.add_command(label = "Fusionner deux bases de données de relations", command=FusionnerDBRelations)
fileMenu.add_command(label = "Fusionner deux bases de données de retours", command=FusionnerDBFeedback)
fileMenu.add_separator()
fileMenu.add_command(label = "Quitter", command=exit)


settingsMenu.add_command(label = "Actualiser la configuration", command=actualiserConfig)
settingsMenu.add_command(label = "Restaurer la configuration par défaut", command=configDefaut)
settingsMenu.add_separator()
settingsMenu.add_command(label = "Configurer", command=afficherConfigMenu)

# création d'onglets
tabs = ttk.Notebook(interface)
tabs.grid(column = 1, row = 0)

# initialisation des frames
mainframe = ttk.Frame(tabs)
relMainframe = ttk.Frame(tabs)
feedbackMainframe = ttk.Frame(tabs)


#########################################################################################################################
#                                                   Gestion des tuteurs                                                 #
#########################################################################################################################
TopFrame = ttk.Frame(mainframe)
EDTFrame = ttk.Frame(mainframe)
BottomFrame = ttk.Frame(mainframe)
OptnFrame = ttk.Frame(mainframe)


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

#label_blank3.grid(columnspan=10, column=0, row=3)
#label_blank10.grid(column = 10, row=0)
#label_blank11.grid(column = 11, row=0)
#label_blank12.grid(column = 12, row=0)

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


#Initialisation des derniers composants
validation.grid(sticky='sw', column=8, row=4)


# activation des frames:
mainframe.pack(fill='both', expand=True)
TopFrame.grid(column = 0, row = 0, columnspan=5)
EDTFrame.grid(sticky ='n', column=0, columnspan=6, row=4, rowspan=12)
BottomFrame.grid(sticky ='s')


#########################################################################################################################
#                                                 Gestion des relations                                                 #
#########################################################################################################################

# Creation de la Frame d'affichage
treeViewFrame = ttk.Frame(relMainframe)

#Affichage de la liste des relations
refreshBTN = ttk.Button(relMainframe, text="Rafraîchir la liste des relations", command=refreshRelPrint)
scrollbar = ttk.Scrollbar(treeViewFrame)
rmBTN = ttk.Button(relMainframe, text="Supprimer la relation", command=delRel)
feedbackBTN = ttk.Button(relMainframe, text="Ajouter/Modifier un avis", command=modifyFeedbackByRel)
endRelBTN = ttk.Button(relMainframe, text="Marque la relation comme terminée", command=finRelation)
principalView = ttk.Treeview(treeViewFrame, column=("c1","c2","c3", "c4", "c5", "c6", "c7"), show='headings', height=25, yscrollcommand=scrollbar.set)
principalView.column("# 1", anchor=tkinter.CENTER,  width = 80)
principalView.heading("# 1", text="relID")
principalView.column("# 2", anchor=tkinter.CENTER,  width = 200)
principalView.heading("# 2", text="Nom tuteur")
principalView.column("# 3", anchor=tkinter.CENTER,  width = 200)
principalView.heading("# 3", text="Prenom tuteur")
principalView.column("# 4", anchor=tkinter.CENTER,  width = 200)
principalView.heading("# 4", text="Nom tutore")
principalView.column("# 5", anchor=tkinter.CENTER,  width = 200)
principalView.heading("# 5", text="Prenom tutore")
principalView.column("# 6", anchor=tkinter.CENTER,  width = 90)
principalView.heading("# 6", text="Matiere")
principalView.column("# 7", anchor=tkinter.CENTER,  width = 150)
principalView.heading("# 7", text="Horaire")
principalView.bind('<Button-1>', selectItemRel)



# activation des composants
treeViewFrame.grid(column=0, row=1, rowspan=40)
principalView.pack(side=tkinter.LEFT, fill=tkinter.Y)
scrollbar.config(command=principalView.yview)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
refreshBTN.grid(column = 1, row= 1)
rmBTN.grid(column=1, row=2)
feedbackBTN.grid(column=1, row=3)
endRelBTN.grid(column=1, row=4)


#########################################################################################################################
#                                                 Gestion des feedbacks                                                 #
#########################################################################################################################

# Creation de la Frame d'affichage
treeViewFrameFeedback = ttk.Frame(feedbackMainframe)

#Affichage de la liste des relations
refreshBTNFeedback = ttk.Button(feedbackMainframe, text="Rafraîchir la liste des avis", command=refreshFeedbackPrint)
scrollbarFeed = ttk.Scrollbar(treeViewFrameFeedback)
rmBTNFeedback = ttk.Button(feedbackMainframe, text="Supprimer l'avis", command=delFeedback)
editBTNFeedback = ttk.Button(feedbackMainframe, text="Editer l'avis", command=modifyFeedbackByFeedback)
feedview = ttk.Treeview(treeViewFrameFeedback, column=("c1","c2","c3", "c4", "c5", "c6", "c7","c8", "c9", "c10"), show='headings', height=25, yscrollcommand=scrollbarFeed.set)
feedview.column("# 1", anchor=tkinter.CENTER,  width = 80)
feedview.heading("# 1", text="feedbackID")
feedview.column("# 2", anchor=tkinter.CENTER,  width = 200)
feedview.heading("# 2", text="Nom tuteur")
feedview.column("# 3", anchor=tkinter.CENTER,  width = 200)
feedview.heading("# 3", text="Prenom tuteur")
feedview.column("# 4", anchor=tkinter.CENTER,  width = 200)
feedview.heading("# 4", text="Nom tutore")
feedview.column("# 5", anchor=tkinter.CENTER,  width = 200)
feedview.heading("# 5", text="Prenom tutore")
feedview.column("# 6", anchor=tkinter.CENTER,  width = 60)
feedview.heading("# 6", text="Caractère")
feedview.column("# 7", anchor=tkinter.CENTER,  width = 90)
feedview.heading("# 7", text="Matiere")
feedview.column("# 8", anchor=tkinter.CENTER,  width = 60)
feedview.heading("# 8", text="Efficacité")
feedview.column("# 9", anchor=tkinter.CENTER,  width = 80)
feedview.heading("# 9", text="RelID")
feedview.column("# 10", anchor=tkinter.CENTER,  width = 150)
feedview.heading("# 10", text="Commentaires")
feedview.bind('<Button-1>', selectItemFeedback)


# activation des composants
treeViewFrameFeedback.grid(column=0, row=1, rowspan=40)
feedview.pack(side=tkinter.LEFT, fill=tkinter.Y)
scrollbar.config(command=feedview.yview)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
refreshBTNFeedback.grid(column = 1, row= 1)
rmBTNFeedback.grid(column=1, row=2)
editBTNFeedback.grid(column=1, row=3)

# Ajout des onglets
tabs.add(mainframe, text="Gestion des tuteurs")
tabs.add(relMainframe, text="Gestion des relations")
tabs.add(feedbackMainframe, text="Gestion des retours")

#Appel de l'init du programme
init()

#Lancement de l'IUG
interface.mainloop()
