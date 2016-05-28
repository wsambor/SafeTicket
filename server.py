from flask import Flask, request, jsonify, render_template
import json
import crud
import show_db
app = Flask(__name__)

@app.route('/')
def index():
	print ("DUPAAA")
	return render_template('index.html')

@app.route('/api/user/login', methods = ['POST'])
def login():
	return(crud.login(request.json))

@app.route('/api/user/pre-register', methods = ['POST', 'GET'])
def pre_register():
	return(crud.pre_register(request.json))

@app.route('/api/user/register', methods = ['POST', 'GET'])
def post():
	return(crud.register(request.json))

@app.route('/api/tickets/<city>', methods = ['POST', 'GET'])
def cityinfo(city):
	return crud.return_city_info(city)

@app.route('/api/tickets/timeticket', methods = ['POST', 'GET'])
def time_ticket():
	return (crud.buyTimeTicket(request.json))

@app.route('/database')
def show():
	rows=showDB.SelectAll()
	return render_template('showDB.html', data=rows)

if __name__ == '__main__':
	app.debug=True
	app.run(port=8000)
	#app.run(host='0.0.0.0')
