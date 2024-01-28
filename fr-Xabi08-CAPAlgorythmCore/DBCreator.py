import sqlite3
CoreLibs = __import__("fr-Xabi08-CAPAlgorythmCore", globals(), locals(), ["groupes"],0)


def createDB(relEnabled = False, feedbackEnabled = False):
    """Create data storage in data.db"""
    connectDB = sqlite3.connect("data.db")
    cursor = connectDB.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'group'(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        label TEXT NOT NULL,
        level INT NOT NULL
    )""")
    connectDB.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'tuteur'(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        groupid INTEGER NOT NULL,
        freeon TEXT NOT NULL,
        subject TEXT NOT NULL,
        FOREIGN KEY (groupid) REFERENCES 'group'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED
        )
        """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'tutore'(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        groupid INTEGER NOT NULL,
        freeon TEXT NOT NULL,
        subject TEXT NOT NULL,
        FOREIGN KEY (groupid) REFERENCES 'group'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED
        )""")
    connectDB.commit()
    if relEnabled:
        cursor.execute("""CREATE TABLE IF NOT EXISTS relation(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            tuteurid INTEGER NOT NULL,
            tutoreid INTEGER NOT NULL,
            lessonsnumber INT,
            time TEXT NOT NULL,
            subject TEXT NOT NULL,
            feedbackid INTEGER,
            FOREIGN KEY (tuteurid) REFERENCES 'tuteur'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED,
            FOREIGN KEY (tutoreid) REFERENCES 'tutore'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED,
            FOREIGN KEY (feedbackid) REFERENCES 'retour'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED 
            )""")
    if feedbackEnabled:
        cursor.execute("""CREATE TABLE IF NOT EXISTS retour(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            tuteurid INTEGER NOT NULL,
            tutoreid INTEGER NOT NULL,
            subject TEXT NOT NULL,
            time TEXT NOT NULL,
            efficiencyscore INT NOT NULL,
            socialscore INT NOT NULL,
            commentary TEXT,
            FOREIGN KEY (tuteurid) REFERENCES 'tuteur'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED,
            FOREIGN KEY (tutoreid) REFERENCES 'tutore'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED
            )
            """)
    connectDB.commit()
    fillGroupTable(connectDB)
    connectDB.close()
    return


def createRelTable():
    connectDB = sqlite3.connect("data.db")
    cursor = connectDB.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS relation(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            tuteurid INTEGER NOT NULL,
            tutoreid INTEGER NOT NULL,
            lessonsnumber INT,
            time TEXT NOT NULL,
            subject TEXT NOT NULL,
            feedbackid INTEGER,
            FOREIGN KEY (tuteurid) REFERENCES 'tuteur'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED,
            FOREIGN KEY (tutoreid) REFERENCES 'tutore'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED,
            FOREIGN KEY (feedbackid) REFERENCES 'retour'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED 
            )""")
    cursor.close()
    connectDB.commit()
    connectDB.close()
    return


def createFeedbackTable():
    connectDB = sqlite3.connect("data.db")
    cursor = connectDB.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS retour(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            tuteurid INTEGER NOT NULL,
            tutoreid INTEGER NOT NULL,
            subject TEXT NOT NULL,
            time TEXT NOT NULL,
            efficiencyscore INT NOT NULL,
            socialscore INT NOT NULL,
            commentary TEXT,
            FOREIGN KEY (tuteurid) REFERENCES 'tuteur'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED,
            FOREIGN KEY (tutoreid) REFERENCES 'tutore'(id) ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE INITIALLY DEFERRED
            )
            """)
    cursor.close()
    connectDB.commit()
    connectDB.close()
    return


def fillGroupTable(DB):
    baseGroups = [["2E1","2E2","2E3","2E4","2E5","2E6"],["1TC1","1TC2","1TC3","1TC4","1TC5"],["TE1","TE2","TE3","TE4"]]
    for i in range(len(baseGroups)):
        for j in range(len(baseGroups[i])):
            CoreLibs.groupes.addGroup(baseGroups[i][j], len(baseGroups)-i,DB)
    return