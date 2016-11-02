import csv
import urllib
#from pathlib2 import Path

def exportToCSV(rows):
	tempfilename = "temp.csv"
	ofile  = open(tempfilename, "wb")
	writer = csv.writer(ofile, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)
	for row in rows:
		writer.writerow(row)
	ofile.close()
	filecontents = open(tempfilename, 'r').read()
	filecontents = '"Date", "Rating", "First Name", "Last Name", "Email", "Comments", "Time of Comment"\n' + filecontents
	return filecontents

