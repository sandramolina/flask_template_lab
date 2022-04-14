from flask import render_template, request
from app import app
from models.event_list import *

@app.route('/')
def home():
    return render_template("index.html", title="Home", events = event_list)

# @app.route('/addevent'):
# def add_event():
