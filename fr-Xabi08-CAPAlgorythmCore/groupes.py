CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["utils"],0)

def groupGetLVL(gname):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT level FROM 'group' WHERE label = ?""",(gname,))
    results = cursor.fetchall()
    cursor.close()
    return results


def addGroup(gname,level):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""INSERT INTO 'group'(label,level) VALUES (?,?)""",(gname,level))
    MainDB.commit()
    return cursor.close()


def getGroupByName(gname):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""SELECT * FROM 'group' WHERE label = ?""",(gname,))
    results = cursor.fetchall()
    cursor.close()
    return results


def rmGroup(gid):
    MainDB = CoreLibs.utils.MainDB
    cursor = MainDB.cursor()
    cursor.execute("""DELETE FROM 'group' WHERE id = ?""",(gid,))
    MainDB.commit()
    return cursor.close()