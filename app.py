# app.py
import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from street_request import street_finder

# create app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# load sensitive data
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
@cross_origin()
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

app.register_blueprint(street_finder)
