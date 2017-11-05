# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

from flask import Flask
import requests
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

app = Flask(__name__)

@app.route("/")
def index():
    """data = db.child("data").get()"""
    return requests.get('https://qr-cart.firebaseio.com/data.json').content


@app.route("/customers")
def customers():
    return requests.get('https://qr-cart.firebaseio.com/data/customers.json').content

@app.route("/customers/<string:phone>/")
def getCustomers(phone):
    return requests.get('https://qr-cart.firebaseio.com/data/customers.json').content

@app.route("/products")
def products():
    return "Members"


@app.route("/products/<string:product_id>/")
def getProduct(product_id):
    return product_id

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, ssl_context='adhoc')
# [END app]
