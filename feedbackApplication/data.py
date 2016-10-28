import sqlite3
import random

sqlite_file = 'globalmamasurvey.db'

def connect(sqlite_file):
	conn = sqlite3.connect(sqlite_file)
	return conn

def close_connection(conn):
	# close the connection passed in
	conn.commit()
	conn.close()

def get_survey_data(cursor):
	query = "select DateofComment, rating, FirstName, LastName, Email, Comment, TimeOfComment  from surveyData"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	return all_rows

def get_store_data(cursor):
	query = "select * from store"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	return all_rows

def fetchDataSet(cursor, query):
	cursor.execute(query)
        all_rows = cursor.fetchall()
        numberOfRows = len(all_rows)
	return numberOfRows, all_rows

def getTotalRatings(cursor):
	query = "Select storeid, rating, count(rating) as number from surveyData group by rating, storeid"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	return all_rows

def getaggRatings(cursor):
	print "Averge Rating Per Store"
	query = "SELECT storeid, avg(rating) as 'Average Rating' FROM surveyData group by storeid"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	return all_rows[0]

def addSurveyData(cursor, surveyRow):
	query = """INSERT INTO surveyData (storeid,rating,FirstName,LastName,Email,Comment)  VALUES ({storeid},{rating},'{FirstName}',
		'{LastName}','{Email}','{Comment}')""".format(storeid=surveyRow[0], rating=surveyRow[1], FirstName=surveyRow[2],
		LastName=surveyRow[3], Email=surveyRow[4], Comment= surveyRow[5])
	cursor.execute(query)

def addAdmin(cursor, userID, password):
	query = """INSERT INTO admin ("user_id","password") VALUES ('{user}','{pwd}')""".format(user=userID, pwd=password)
	cursor.execute(query)

def userExists(cursor, userID):
	query = "select count(*) from admin where user_id = '{user}'".format(user=userID)
	cursor.execute(query)
	all_rows = cursor.fetchall()
	return all_rows[0][0] > 0

def loginValid(cursor, userID, password):
	query = "select count(*) from admin where user_id = '{user}' and password = '{pwd}'".format(user=userID, pwd=password)
        cursor.execute(query)
        all_rows = cursor.fetchall()
        return all_rows[0][0] > 0

def populateData(cursor):
	FirstNames = ('John','Bob','Tim','Mike','Eric','Sam','Ed','Mary','Liz','Nicole','Rebecca','Lisa','Alicia','Tiffany')
	LastNames = ('Smith','Brown','Anderson','Clark','Black','Blake','Rice','Sanders','Clinton','Robinson','Kane','Trent')
	Emails = ('gmail.com','hotmail.com','yahoo.com','mail.com','netmail.com','juno.com','facebook.com','to.com')
	randomFirstName = FirstNames[random.randint(0,13)]
	randomLastName = LastNames[random.randint(0,11)]
	randomEmail = randomFirstName + "." +randomLastName+ str(random.randint(0,1500)) +"@"+Emails[random.randint(0,7)]
	data = (1,random.randint(1,5),randomFirstName, randomLastName, randomEmail,'')
	addSurveyData(cursor, data)
	print data

if __name__ == '__main__':
	conn, c = connect(sqlite_file)
	get_survey_data(c)
	#get_store_data(c)
	#addSurveyData(data)
	getTotalRatings(c)
	getaggRatings(c)
	close_connection(conn)
