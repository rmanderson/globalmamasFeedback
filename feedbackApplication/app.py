from flask import Flask, request, make_response, render_template, session, redirect, url_for
import data
import datetime
import exportdata

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/feedback")
def feedback():
    return app.send_static_file('form.html')

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
	return app.send_static_file('thankyou.html')
    else:
        error = 'Invalid username/password'

@app.route('/login', methods=['POST', 'GET'])
def showlogin():
    error = None
    if request.method == 'POST':
	username = request.form['login']
	password =request.form['pwd']
	resp = setcookieandredirect(username)
	return resp
	return render_template('login.html', msg="Failed to login")
    else:
	if 'username' in session:
		resp = make_response(render_template('admin.html'))
		return resp
	else:
    		return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

def setcookieandredirect(user):
    resp = make_response(render_template('admin.html'))
    session['username'] = user
    return resp

@app.route('/downloadData')
def getfeedbackdata():
    conn = data.connect('globalmamasurvey.db')
    rows = data.get_survey_data(conn.cursor())
    csv = exportdata.exportToCSV(rows)
    response = make_response(csv)
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response

if __name__ == "__main__":
    app.run()
