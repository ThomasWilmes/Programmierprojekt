"""
Implementation of Programming Project Flask API
"""
import os

from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
from recommendation import *

# enables flask
app = Flask(__name__)

# enables CORS
CORS(app)
api = Api(app)


@app.route('/movies', methods=['GET'])
def get_mov_list():
    """Return the Full Movie List"""
    return get_movie_list()


@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    """
    If more than one ID is entered, creates an array from the IDs entered with commas and calls the get_list_of_recommendation method if there are no more than five IDs entered.
    """
    request_data = request.args.get('movie_id')
    if (request_data is None):
        return 'Please enter a value for the key: "movie_id"', 400
    try:
        if ',' in request_data:
            movie_ids = [int(mov) for mov in request_data.split(',')]
            if (len(movie_ids) > 5):
                return 'Only five movies can be entered at the same time', 400
        else:
            movie_ids = [int(request_data)]
        return get_list_of_recommendation(movie_ids)
    except Exception as e:
        return 'The input data is not in the correct format. The message was: ({0})'.format(e), 400



if __name__ == '__main__':
    """
configures the port and hosting for the flask api
    """
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port)