import sqlite3

sqlite_file = 'globalmamasurvey.db'

def connect(sqlite_file):
        conn = sqlite3.connect(sqlite_file)
        return conn

def close_connection(conn):
        # close the connection passed in
        conn.commit()
        conn.close()

def createSurveyTable(conn):
	c = conn.cursor()
	surveyDataTable = 'CREATE  TABLE  IF NOT EXISTS "main"."surveyData" ("id" INTEGER PRIMARY KEY  NOT NULL , "storeid" INTEGER NOT NULL , "rating" INTEGER, "FirstName" VARCHAR, "LastName" VARCHAR, "Email" VARCHAR, "Comment" TEXT, "DateOfComment" DATETIME NOT NULL  DEFAULT CURRENT_DATE, "TimeOfComment" DATETIME NOT NULL  DEFAULT CURRENT_TIME)'
	c.execute(surveyDataTable)

def createAdminTable(conn):
	c = conn.cursor()
	adminDataTable = "CREATE  TABLE 'main'.'admin' ('id' INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL , 'user_id' VARCHAR NOT NULL  UNIQUE , 'password' VARCHAR NOT NULL )"
	c.execute(adminDataTable)

def createDatabaseTables():
	conn = connect(sqlite_file)
	createSurveyTable(conn)
	createAdminTable(conn)
	close_connection(conn)

def checkAdminTableHasUsers():
	conn = connect(sqlite_file)
        adminTableCheck = "SELECT count(*) FROM admin"
        c = conn.cursor()
        c.execute(adminTableCheck)
        all_rows = c.fetchall()
        numberOfRows = all_rows[0][0]
        close_connection(conn)
        return numberOfRows

def checkAdminTableExists():
	conn = connect(sqlite_file)
	adminTableCheck = "SELECT name FROM sqlite_master WHERE type='table' AND name= 'admin'"
	c = conn.cursor()
	c.execute(adminTableCheck)
	all_rows = c.fetchall()
        numberOfRows = len(all_rows)
	close_connection(conn)
	return numberOfRows

def checkSurveyTableExists():
	conn = connect(sqlite_file)
        adminTableCheck = "SELECT name FROM sqlite_master WHERE type='table' AND name= 'surveyData'"
        c = conn.cursor()
        c.execute(adminTableCheck)
        all_rows = c.fetchall()
        numberOfRows = len(all_rows)
        close_connection(conn)
        return numberOfRows
