import sqlite3

sqlite_file = 'globalmamasurvey.db'

def connect(sqlite_file):
        conn = sqlite3.connect(sqlite_file)
        return conn

def close_connection(conn):
        # close the connection passed in
        conn.commit()
        conn.close()

def checkdatabasetables(conn):
	c = conn.cursor()
	surveyDataTable = 'CREATE  TABLE  IF NOT EXISTS "main"."surveyData" ("id" INTEGER PRIMARY KEY  NOT NULL , "storeid" INTEGER NOT NULL , "rating" INTEGER, "FirstName" VARCHAR, "LastName" VARCHAR, "Email" VARCHAR, "Comment" TEXT, "DateOfComment" DATETIME NOT NULL  DEFAULT CURRENT_DATE, "TimeOfComment" DATETIME NOT NULL  DEFAULT CURRENT_TIME)'
	c.execute(surveyDataTable)

def checkdatabase():
	conn = connect(sqlite_file)
	checkdatabasetables(conn)
	close_connection(conn)
