import csv
import sqlite3
import os


def createDB(relEnabled = False, feedbackEnabled = False):
    """Create data storage in data.db"""
    connectDB = sqlite3.connect("data.db")
    cursor = connectDB.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS tuteur(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        group INTEGER NOT NULL REFERENCES group(id),
        freeon TEXT NOT NULL,
        subjects TEXT NOT NULL)
        """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS tutore(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        grade INTEGER NOT NULL,
        group INTEGER NOT NULL REFERENCES group(id),
        freeon TEXT NOT NULL,
        subjects TEXT NOT NULL)""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS group(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        label TEXT NOT NULL,
        level INT NOT NULL,
    )""")
    if relEnabled:
        cursor.execute("""CREATE TABLE IF NOT EXISTS relation(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            tuteurid INTEGER NOT NULL REFERENCES tuteur(id),
            tutoreid INTEGER NOT NULL REFERENCES tutore(id),
            lessonsnumber INT,
            subject TEXT NOT NULL,
            FOREIGN KEY (tuteurid) REFERENCES tuteur (tuteurid),
            FOREIGN KEY (tutoreid) REFERENCES tutore (tutoreid) )""")
    if feedbackEnabled:
        cursor.execute("""CREATE TABLE IF NOT EXISTS retour(
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            tuteurid INTEGER NOT NULL REFERENCES tuteur(id),
            tutoreid INTEGER NOT NULL REFERENCES tutore(id),
            subject TEXT NOT NULL,
            efficiencyscore INT NOT NULL,
            socialscore INT NOT NULL,
            commentary TEXT,
            FOREIGN KEY (tuteurid) REFERENCES tuteur (tuteurid),
            FOREIGN KEY (tutoreid) REFERENCES tutore (tutoreid))
            """)
    connectDB.commit()
    connectDB.close()
    return

