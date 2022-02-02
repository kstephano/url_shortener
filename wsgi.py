from app import app
from models import Path
from models.Path import db

db.drop_all()
db.create_all()

if __name__ == '__main__':
    app.run(debug = True)

