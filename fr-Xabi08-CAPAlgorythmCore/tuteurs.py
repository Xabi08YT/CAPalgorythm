CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)


creneaux = CoreLibs.utils.creneaux


def deleteTuteur(name, surname, groupid):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    delete_rq="DELETE FROM 'tuteur' WHERE name = '"+name+"' AND surname = '"+surname+"' AND groupid = "+str(groupid)
    cursor.execute(delete_rq)
    MainDB.commit()
    cursor.close()
    return 


def addTuteur(name, surname, groupid,parsedFreetime,parsedSubjects):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""INSERT INTO tuteur (name,surname,group,freeon,subject) VALUES (?,?,?,?,?)""",(name,surname,groupid,parsedFreetime,parsedSubjects))
    MainDB.commit()
    return cursor.close()


def findTuteur(groupLVL,parsedFreetime,parsedSubjects):
    results = []
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    freetimes = [i.replace("_","").replace("%","") for i in parsedFreetime]
    creneauxTXT = [CoreLibs.utils.creneaux[i.replace("_","").replace("%","")] for i in parsedFreetime]
    subjects = [i.replace("_","").replace("%","") for i in parsedSubjects]
    for i in parsedFreetime:
        for j in parsedSubjects:
            cursor.execute("""SELECT 'tuteur'.id,name, surname FROM 'tuteur' INNER JOIN 'group' ON 'tuteur'.groupid = 'group'.id WHERE 'group'.level <= ? AND freeon LIKE ? AND subject LIKE ?""",(groupLVL,i,j))
            tmp = cursor.fetchall()
            results.append(tmp)
            print(i,j,tmp)
    cursor.close()
    return {"creneaux":freetimes,"subjects":subjects,"creneauxTXT":creneauxTXT,"results":results}