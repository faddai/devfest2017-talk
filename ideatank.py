import os
import hashlib

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

secret = os.environ.get('IDEATANK_SECRET_KEY')
db_user = os.environ.get('IDEATANK_DB_USER')
db_password = os.environ.get('IDEATANK_DB_PASSWORD', '')
db_host = os.environ.get('IDEATANK_DB_HOST', 'localhost')

app = Flask(__name__)
app.secret_key = secret
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/ideatank'.format(db_user, db_password, db_host)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()