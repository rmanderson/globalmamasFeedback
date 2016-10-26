import csv
import urllib
from pathlib2 import Path

def exportToCSV(rows):
	ofile  = open('ttest.csv', "wb")
	writer = csv.writer(ofile, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)
	for row in rows:
		writer.writerow(row)
	#filecontents = ofile.content
	ofile.close()
	contents = Path('ttest.csv').read_text()
	return filecontents

