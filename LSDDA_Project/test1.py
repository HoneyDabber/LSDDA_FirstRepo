'''
Created on Mar 14, 2017

@author: Awais
'''

# from http://flask.pocoo.org/ tutorial
from flask import Flask
app = Flask(__name__)

@app.route("/") # take note of this decorator syntax, it's a common pattern
def hello():
    return "Hello World!"


@app.route('/aboutMe')
def aboutMe():
    return "All about 'about' "
    
if __name__ == "__main__":
    app.run()