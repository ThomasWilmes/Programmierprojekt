"""
Test implementation of a Restful API
"""
import os

from flask import Flask, request, jsonify
from flask_restful import Api
from recommendation import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)


@app.route('/movies', methods=['GET'])
def get_list():
    """Return the Full Movie List"""
    return get_movie_list()

@app.route('/with_parameters')
def with_parameters():
    """Returns the recommendation"""
    film_name = request.args.get('filmname')
    film_id = int(request.args.get('filmid'))
    return jsonify(message="The Film: " + str(film_name) + " has the ID:" + film_id)

@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    """
    Recommendations Endpoint
    """
    request_data = request.args.get('movies_ids')
    if (request_data is None):
        return 'No input data was given', 400
    try:
        if ',' in request_data:
            movie_id = [int(movie) for movie in request_data.split(',')]
        else:
            movie_id = [int(request_data)]
        return get_movie_list(movie_id)
   

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port, debug=True)
