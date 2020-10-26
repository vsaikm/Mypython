###################################################
#Create an environment -     py  -3  -m venv venv
#Activate the environment - venv\Scripts

from flask import Flask
app = Flask(__name__)
print(app, __name__)

@app.route('/')#decorator--  extra tools to built a ervver
def hello_world():
    return 'Hello, World!'
    
