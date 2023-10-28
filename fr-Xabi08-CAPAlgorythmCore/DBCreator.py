import sqlite3


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
        FOREIGN KEY (groupid) REFERENCES 'group'(id)
        )
        """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS 'tutore'(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        groupid INTEGER NOT NULL,
        freeon TEXT NOT NULL,
        subject TEXT NOT NULL,
        FOREIGN KEY (groupid) REFERENCES 'group'(id)
        )""")
    connectDB.commit()
    if relEnabled:
        cursor.execute("""CREATE TABLE IF NOT EXISTS relation(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            tuteurid INTEGER NOT NULL,
            tutoreid INTEGER NOT NULL,
            lessonsnumber INT,
            subject TEXT NOT NULL,
            feedbackid INTEGER,
            FOREIGN KEY (tuteurid) REFERENCES 'tuteur'(tuteurid),
            FOREIGN KEY (tutoreid) REFERENCES 'tutore'(tutoreid),
            FOREIGN KEY (feedbackid) REFERENCES 'retour'(id) 
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
            FOREIGN KEY (tuteurid) REFERENCES 'tuteur'(tuteurid),
            FOREIGN KEY (tutoreid) REFERENCES 'tutore'(tutoreid)
            )
            """)
    connectDB.commit()
    connectDB.close()
    return

