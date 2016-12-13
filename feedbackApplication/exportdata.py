import csv
import urllib
#from pathlib2 import Path

def exportToCSV(rows):
	tempfilename = "temp.csv"
	ofile  = open(tempfilename, "wb")
	writer = csv.writer(ofile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	for row in rows:
		writer.writerow(row)
	ofile.close()
	filecontents = open(tempfilename, 'r').read()
	filecontents = '"Date"\t"Rating"\t"First Name"\t"Last Name"\t"Email"\t"Comments"\t"Time of Comment"\n' + filecontents
	return filecontents

