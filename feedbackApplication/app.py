from flask import Flask
from flask import request
import data

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run()
