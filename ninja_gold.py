from flask import Flask, render_template, request, redirect, session
import random
import datetime

app = Flask(__name__)
app.secret_key = 'codingdojo'

@app.route("/")
def landing():
	if not 'result' in session:
		session['message'] = []
		session['result'] = 0
	return render_template("ninja_gold.html")

@app.route("/process_money", methods = ['POST'])
def find_gold():
	if request.form['building'] == 'farm':
		session['newearn'] = random.randint(10,20)
		session['result'] += session['newearn']
		session['message'].append('Earned ' + str(session['newearn']) + ' golds from the farm!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
		return redirect("/")
	
	if request.form['building'] == 'cave':
		session['newearn'] = random.randint(5,10)
		session['result'] += session['newearn']
		session['message'].append('Earned ' + str(session['newearn']) + ' golds from the cave!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
		return redirect("/")

	if request.form['building'] == 'house':
		session['newearn'] = random.randint(2,5)
		session['result'] += session['newearn']
		session['message'].append('Earned ' + str(session['newearn']) + ' golds from the house!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
		return redirect("/")

	if request.form['building'] == 'casino':
		session['newearn'] = random.randint(-50,50)
		session['result'] += session['newearn']
		if session['newearn'] >= 0:
			session['message'].append('Entered a casino and earned ' + str(session['newearn']) + ' golds from the casino!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
		elif session['newearn'] < 0:
			if session['result'] >= 0:
				session['message'].append('Entered a casino and lost ' + str(abs(session['newearn'])) + ' golds from the casino!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
			elif session['result'] < 0:
				session['message'].append('Now you owe us ' + str(session['result']) + ' gold!')
		return redirect("/")

@app.route('/reset', methods = ['POST'])
def reset():
	session['message'] = []
	session['result'] = 0
	return redirect('/')

app.run(debug = True)