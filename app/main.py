"""
Test implementation of a Restful API
"""
import os

from flask import Flask, request
from flask_restful import Api
from recommendation import *

app = Flask(__name__)
api = Api(app)


@app.route("/test")
def hello_world():
    return "<p>Testpage!</p>"

@app.route('/movies')
def get_movies():
    return getListOfMovies()


@app.route('/recommendation')
def get_recommendation():
    requestData = request.form.get('movies')
    if (requestData is None):
        return 'No input data was given', 400
    movieList = requestData.split(',')
    if (movieList is None):
        return 'The input data is not in the correct format', 400
    return getListOfRecommendations(movieList)


if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port, debug=True)
