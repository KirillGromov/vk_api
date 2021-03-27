from flask import Flask
from config import Configuration
from model import *

app = Flask(__name__)
app.config.from_object(Configuration)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fwniwhcuymyrgb:edab885706990eec1a47223ef9da80545b69ded4362e5f045412cc8601bf87c8@ec2-54-155-208-5.eu-west-1.compute.amazonaws.com:5432/dtucdfgtb5250'

db = SQLAlchemy(app)
