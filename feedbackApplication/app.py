from flask import Flask, request, make_response, render_template, session, redirect, url_for
import data
import datetime
import exportdata
import setup
import time

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def hello():
    return feedback()

@app.route("/feedback")
def feedback():
    if isDatabaseReady():
    	return render_template('form.html')
    else:
	return render_template('setadmin.html', msg="Please Create an Admin Login")

@app.route('/processform', methods=['POST'])
def processform():
    error = None
    if request.method == 'POST':
	firstname = request.form['firstname']
	lastname = request.form['lastname']
	rating = request.form['rating']
	email = request.form['email']
	comments = request.form['comment']
	conn = data.connect('globalmamasurvey.db')
	rowdata = (1,rating,firstname,lastname,email,comments)
	data.addSurveyData(conn.cursor(),rowdata)
	data.close_connection(conn)
	return render_template('thankyou.html')
    else:
        error = 'Invalid username/password'

@app.route('/login', methods=['POST', 'GET'])
def showlogin():
    error = None
    if request.method == 'POST':
	username = request.form['login']
	password = request.form['pwd']
	if loginverified(username, password):
		resp = setcookieandredirect(username)
		return resp
	else:
		return render_template('login.html', msg="Failed to login")
    else:
	if 'username' in session:
		resp = make_response(render_template('admin.html'))
		return resp
	else:
    		return render_template('login.html')

@app.route('/adduser', methods=['POST'])
def adduser():
    error = None
    if request.method == 'POST':
	username = request.form['login']
	password = request.form['pwd']
	conn = data.connect('globalmamasurvey.db')
	if data.userExists(conn.cursor(), username):
		return render_template('setadmin.html', msg="User Exists")
	else:
		data.addAdmin(conn.cursor(), username, password)
		data.close_connection(conn)
		return render_template('form.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('showlogin'))

def setcookieandredirect(user):
    resp = make_response(render_template('admin.html'))
    session['username'] = user
    return resp

def isDatabaseReady():
    if setup.checkAdminTableExists() == 0 or setup.checkSurveyTableExists() == 0:
	setup.createDatabaseTables()
	return False
    else:
	if setup.checkAdminTableHasUsers() > 0:
		return True
	else:
		return False

def loginverified(username, password):
    conn = data.connect('globalmamasurvey.db')
    return data.loginValid(conn.cursor(), username, password)

@app.route('/downloadData', methods=['POST', 'GET'])
def getfeedbackdata():
    conn = data.connect('globalmamasurvey.db')
    rows = data.get_survey_data(conn.cursor())
    csv = exportdata.exportToCSV(rows)
    epoch_time = int(time.time())
    outputfilename = str(epoch_time) + ".csv" 
    response = make_response(csv)
    response.headers["Content-Disposition"] = "attachment; filename="+outputfilename
    return response

if __name__ == "__main__":
    app.run()
