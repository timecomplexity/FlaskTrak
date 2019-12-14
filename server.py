from flask import Flask, request, render_template
import MySQLdb
import json

app = Flask(__name__, static_url_path='/static', template_folder='template')

# Application routes determine the functions to call when the user tries to access a particular URL
@app.route('/')
def server_init():
	return render_template("index.html", title='FlaskTrak - Track your stuff!')
