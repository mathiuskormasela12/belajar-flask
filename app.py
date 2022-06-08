from flask import Flask, render_template, request

app = Flask(__name__)

"""
	A. Menjalankan Flask

	Dengan mode debug :
	FLASK_APP=app FLASK_DEBUG=1 flask run

	Tanpa Mode Debug :
	FLASK_APP=app flask run
"""

# Render Template HTML
@app.route('/')
def home() :
	return render_template('index.html', title='Home', name='Mathius')

# req.params
@app.route('/test/<nama>')
def login(nama) :
	return f'<h1>Hello {nama}</h1>'

# req.params dengan tipe data
@app.route('/test2/<int:id>')
def register(id) :
	return f'<h1>{id} adalah id nya</h1>'

# Form Handling
@app.route('/signin', methods=['POST', 'GET'])
def signin() :
	if request.method == 'POST' :
		return f'Username kamu adalah {request.form["username"]} dan password kamu adalah {request.form["password"]}'
		
	return render_template('login.html', title='Sign In')

