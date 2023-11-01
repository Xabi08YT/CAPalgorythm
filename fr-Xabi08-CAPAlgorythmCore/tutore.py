CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)


creneaux = CoreLibs.utils.creneaux


def deleteTutore(name, surname, groupid):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    delete_rq="DELETE FROM 'tutore' WHERE name = '"+name+"' AND surname = '"+surname+"' AND groupid = "+str(groupid)
    cursor.execute(delete_rq)
    MainDB.commit()
    cursor.close()
    return 


def addTutore(name, surname, groupid,parsedFreetime,parsedSubjects):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""INSERT INTO 'tutore' (name,surname,groupid,freeon,subject) VALUES (?,?,?,?,?)""",(name,surname,groupid,parsedFreetime,parsedSubjects))
    MainDB.commit()
    return cursor.close()


def getTutoreID(name,surname,gid):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT id FROM 'tutore' WHERE surname = ? AND name = ? and groupid = ?""",(surname,name,gid))
    tmp = cursor.fetchall()
    cursor.close()
    return tmp


def getTutoreNomByID(id):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT name,surname FROM 'tutore' WHERE id = ?""",(id,))
    tmp = cursor.fetchall()
    cursor.close()
    return tmp