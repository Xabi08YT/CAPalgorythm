CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)


def addFeedback(tuteurid,tutoreid,subject,time,effScore,socScore,com = None):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""INSERT INTO retour (tuteurid,tutoreid,subject,time,efficiencyscore,socialscore,commentary) VALUES (?,?,?,?,?,?,?)""",(tuteurid,tutoreid,subject,time,effScore,socScore,com))
    MainDB.commit()
    return


def modifyFeedback(id,effscore,soscore,comm):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""UPDATE retour SET efficiencyscore = ?, socialscore = ?, commentary = ? WHERE id = ?""",(effscore,soscore,comm,id))
    MainDB.commit()
    return


def delFeedback(id):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""DELETE FROM retour WHERE id=?""",(id,))
    MainDB.commit()
    return


def getFeedback(id):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT * FROM retour WHERE id=?""",(id,))
    return cursor.fetchall()


def getAllFeedbacks():
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT * FROM retour""")
    return cursor.fetchall()