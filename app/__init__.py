from flask import Flask
from os.path import dirname, join
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI="sqlite:///" + join(dirname(dirname(__file__)), "database.sqlite"),
)

db = SQLAlchemy(app)
ma = Marshmallow(app)



from app.views import employee_view

