'''
Recipy is a python based recipe tracker. The idea is that it will sort recipes
based on certain attributes such as time/food required/kitchen utencils etc.


'''

from app import app
from flask import render_template

@app.route("/")
def main():
    return render_template('index.html')
