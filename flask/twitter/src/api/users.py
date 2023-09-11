from flask import Blueprint
from ..models import User, db, Tweet, likes_table

db = Blueprint('users', __name__, url_prefix='/users')