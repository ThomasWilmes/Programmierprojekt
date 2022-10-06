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


@app.route('/movies')
def get_list():
"""Return the Full Movie List"""
    return getMovieList()

@app.route('/with_parameters')
def with_parameters():
    """Returns the recommendation"""
    film_name = request.args.get('filmname')
    film_id = int(request.args.get('filmid'))
    return jsonify(message="The Film: " + str(film_name) + " has the ID:" + film_id)

if __name__=='__main__':
    cfg_port = os.getenv('PORT', "5000")
    app.run(host="0.0.0.0", port=cfg_port, debug=True)
