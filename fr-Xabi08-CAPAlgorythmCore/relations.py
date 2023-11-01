CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)

def addRelationship(tuteurid,tutoreid,subject,time,lessons,feedbackid = None):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""INSERT INTO 'relation' (tuteurid,tutoreid,lessonsnumber,time,subject,feedbackid) VALUES (?,?,?,?,?,?)""",(tuteurid,tutoreid,lessons,time,subject,feedbackid))
    MainDB.commit()
    cursor.close()
    return


def modifyRelationship(id,lessons,feedbackid = None):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""UPDATE 'relation' SET feedbackid = ?, lessonsnumber = ? WHERE id = ?""",(feedbackid,lessons,id))
    MainDB.commit()
    return


def delRelationship(id):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""DELETE FROM 'relation' WHERE id=?""",(id,))
    MainDB.commit()
    return


def getRelationship(id):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT * FROM 'relation' WHERE id=?""",(id,))
    return cursor.fetchall()


def getAllRelationships():
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT * FROM 'relation'""")
    return cursor.fetchall()