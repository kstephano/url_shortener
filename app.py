from flask import Flask, render_template
from flask_cors import CORS
from werkzeug import exceptions
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///models/db/urls.db'
db = SQLAlchemy(app)

from routes import paths

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('home.html', url_short=''), 404
