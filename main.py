# [START app]
import logging

from flask import Flask, request, url_for
from datetime import datetime, timedelta
import requests
import json
from flask_jsonpify import jsonify
"""import pyrebase"""

"""
config = {
  "authDomain": "qr-cart.firebaseapp.com",
  "databaseURL": "https://qr-cart.firebaseio.com",
  "storageBucket": "qr-cart.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
"""

# init
app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
	return ("index ok")

# shared methods
@app.route("/login")
def login():
	# param: phoneno
	# if on system
		# if agent
			# return phoneno=phoneno, authenticated=2
		# else is cx
			# return phoneno=phoneno, authenticated=1
	# else return phone=phone, authenticated=0
	phone = str(request.args.get('phone'))
	cxs = requests.get('https://qr-cart.firebaseio.com/data/customers.json').json()
	for cx in cxs:
		if cx is not None and cx['phone'] == phone:
			return (jsonify({'phone' : cx['phone'], 'authenticated' : 1}))
	ags = requests.get('https://qr-cart.firebaseio.com/data/agents.json').json()
	for ag in ags:
		if ag is not None and ag['phone'] == phone:
			return (jsonify({'phone' : ag['phone'], 'authenticated' : 2}))
	return (jsonify({'phone' : phone, 'authenticated' : 0}))

@app.route("/getCart")
def getCart():
	# param: phoneno
	# init empty cart json
	# get database json search by cx phoneno
	# if no cart
		# return empty cart
	# else
		# return cart
	phone = str(request.args.get('phone'))
	cx = requests.get(url_for('getCust', phone=phone, _external=True)).json()
	return (jsonify(cx))

@app.route("/getTotal")
def getTotal():
	# param: phoneno
	# init total = 0
	# if getCart() is empty
		# return 0
	# else
		# for item in cart
			# total += getValue(itemNo)
		# return total
	return ("temp getTotal")

@app.route("/productImg/")
def getProductImg():
	# param: itemno
	# get prodimg json search with itemno
	# return img
	return ("tmp prod img")

# agent methods
@app.route("/allCustomers")
def allCustomers():
	# no param
	# get json requests.get('https://qr-cart.firebaseio.com/data/customers.json').content
	# clean up
	# return
    return requests.get('https://qr-cart.firebaseio.com/data/customers.json').content

@app.route("/getCust")
def getCust():
	phone = str(request.args.get('phone'))
	cxs = requests.get('https://qr-cart.firebaseio.com/data/customers.json').json()
	for cx in cxs:
		if cx is not None and cx['phone'] == phone:
			return (jsonify(cx))
	return ("not found")

@app.route("/confirm")
def confirm():
    return ("confirm payment")

@app.route("/endDay")
def endDay():
	return ("day concluded")

# customer methods
@app.route("/signup")
def signup():
	# routed from login
	return ("tmp signup")

@app.route("/enterStore")
def enterStore():
	return ("tmp enterStore")

@app.route("/sendAlert")
def sendAlert():
	return ("cx nick has entered your store")

@app.route("/addItem")
def addItem():
	return ("tmp item added")

@app.route("/updateQty") # to 0 to remove item
def updateQty():
	return ("tmp item qty updated")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, threaded=True)
# [END app]
