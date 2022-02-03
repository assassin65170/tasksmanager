from flask import render_template,url_for,request
from todo import app

@app.route('/')
def index():
	return "Hello"