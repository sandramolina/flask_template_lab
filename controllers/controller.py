from flask import render_template, request
from app import app
from models.event_list import *

@app.route('/')
def home():
    return render_template("index.html", title="Home", events = event_list)

@app.route('/addevent', methods=['POST'])
def add_event():
    event_date = request.form["date"]
    event_name = request.form["event_name"]
    guest_number = request.form["guest_number"]
    event_address = request.form["address"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name, guest_number, event_address, event_description)
    add_new_event(new_event)
    return render_template("index.html", title="Home", events = event_list)