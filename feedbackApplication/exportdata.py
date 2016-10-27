import csv
import urllib
#from pathlib2 import Path

def exportToCSV(rows):
	ofile  = open('ttest.csv', "wb")
	writer = csv.writer(ofile, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)
	for row in rows:
		writer.writerow(row)
	ofile.close()
	filecontents = open('ttest.csv', 'r').read()
	filecontents = '"Date", "Rating", "First Name", "Last Name", "Email", "Comments", "Time of Comment"' + filecontents
	return filecontents

