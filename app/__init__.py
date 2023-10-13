from flask import Flask

app = Flask(__name__)

from app import views
from app import db_con
from app import db_view