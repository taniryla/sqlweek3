from flask import Blueprint, jsonify, abort, request
from ..models import Tweet, User, db

bp = Blueprint('tweets', __name__, url_prefix='/tweets')

@bp.route('', methods=['GET']) #DECORATOR TAKES PATH AND LIST OF HTT VERBS
def index():
    tweets = Tweet.query.all() # ORM performs SELECT query
    result = []
    for t in tweets:
        result.append(t.serialize()) # build list of Tweets as dictionaries
    return jsonify(result) # return JSON response