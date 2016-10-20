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
	query = "select * from surverydata"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	for row in all_rows:
		print row
	print("Number of rows: {}".format(numberOfRows))

def get_store_data(cursor):
	query = "select * from store"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	print all_rows
	print("Number of rows: {}".format(numberOfRows))

def fetchDataSet(cursor, query):
	cursor.execute(query)
        all_rows = c.fetchall()
        numberOfRows = len(all_rows)
	return numberOfRows, all_rows

def getTotalRatings(cursor):
	query = "Select storeid, rating, count(rating) as number from surveryData group by rating, storeid"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	print "Number of Ratings per store"
	for row in all_rows:
		print row

def getaggRatings(cursor):
	print "Averge Rating Per Store"
	query = "SELECT storeid, avg(rating) as 'Average Rating' FROM surveryData group by storeid"
	numberOfRows, all_rows = fetchDataSet(cursor, query)
	print all_rows[0]

def addSurveyData(cursor, surveyRow):
	query = """INSERT INTO surveryData (storeid,rating,FirstName,LastName,Email,Comment)  VALUES ({storeid},{rating},'{FirstName}',
		'{LastName}','{Email}','{Comment}')""".format(storeid=surveyRow[0], rating=surveyRow[1], FirstName=surveyRow[2],
		LastName=surveyRow[3], Email=surveyRow[4], Comment= surveyRow[5])
	cursor.execute(query)

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
