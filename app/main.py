"""
Test implementation of a Restful API
"""
import os
import pandas as pd

from flask import Flask, request
from flask_restful import Api
from recommendation import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


df = pd.read_csv("data/movie_titles.csv")

@app.route('/movies')
def get_list():
    return getMovieList()

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port, debug=True)
