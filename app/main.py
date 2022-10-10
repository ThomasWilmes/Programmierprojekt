"""
Test implementation of a Restful API
"""
import os

from flask import Flask, request, jsonify
from flask_restful import Api
from recommendation import *
from flask_cors import CORS

app = Flask(__name__)
app.debug = True

CORS(app)
api = Api(app)


@app.route('/movies', methods=['GET'])
def get_mov_list():
    """Return the Full Movie List"""
    return get_movie_list()

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
            if (len(movie_id) > 5):
                return 'No more than five movies can be selected at a time', 400
        else:
            movie_id = [int(request_data)]
        return get_list_of_recommendation(movie_id)
    except Exception as e:
        return 'The message was: ({0})'.format(e), 400

if __name__ == '__main__':
    """
configures the port and hosting for the flask api
    """
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)