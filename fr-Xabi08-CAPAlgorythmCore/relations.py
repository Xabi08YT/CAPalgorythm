CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils","relations"],0)


def addRelationship(tuteurid,tutoreid,subject,lessons,feedbackid = None):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""INSERT INTO relation (tuteurid,tutoreid,lessonsnumber,subject,feedbackid) VALUES (?,?,?,?,?)""",(tuteurid,tutoreid,lessons,subject,feedbackid))
    MainDB.commit()
    return


def modifyRelationship(id,lessons,feedbackid = None):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""UPDATE relation SET feedbackid = ?, lessonsnumber = ? WHERE id = ?"""(feedbackid,lessons,id))
    MainDB.commit()
    return


def delRelationship(id):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""DELETE FROM relation WHERE id=?"""(id,))
    MainDB.commit()
    return


def getRelationship(id):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT * FROM relation WHERE id=?"""(id,))
    return cursor.fetchall()


def getAllRelationships():
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT * FROM relation""")
    return cursor.fetchall()