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
		session['result'] += random.randint(10,20)
		# session['message'].append('Earned ' + str(session['result']) + ' golds from the farm!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
		return render_template("ninja_gold.html")
	
	# if request.form['building'] == 'cave':
	# 	session['result'] += random.randint(10,20)
	# 	# session['message'].append('Earned ' + str(session['result']) + ' golds from the farm!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
	# 	return render_template("ninja_gold.html")

	# if request.form['building'] == 'house':
	# 	session['result'] += random.randint(10,20)
	# 	# session['message'].append('Earned ' + str(session['result']) + ' golds from the farm!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
	# 	return render_template("ninja_gold.html")

	# if request.form['building'] == 'casino':
	# 	session['result'] += random.randint(10,20)
	# 	# session['message'].append('Earned ' + str(session['result']) + ' golds from the farm!(' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ')')
		# return render_template("ninja_gold.html")

@app.route('/reset', methods = ['POST'])
def reset():
	session['message'] = []
	session['result'] = 0
	return redirect('/')

app.run(debug = True)