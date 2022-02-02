from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound
from app import db

class Path(db.Model):
    shortUrl = db.Column(db.String(50), primary_key=True)
    longUrl = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"long: {self.longUrl}, short: {self.shortUrl}"

    @classmethod
    def all(cls):
        urls = Path.query.all()
        urls = list(map(serialize, urls))
        return urls

    def findByShortUrl(url):
        try:
            print("findByShortUrl")
            path = Path.query.get_or_404(url)
            print("path short url: ", path.shortUrl)
            return path
        except:
            raise NotFound(f"Path with url {url} does not exist!")

    def create(longUrl, shortUrl):
        new_url = Path(longUrl=longUrl, shortUrl=shortUrl)
        db.session.add(new_url)
        db.session.commit()
        return serialize(new_url)

def serialize(self):
    return {
        "longUrl": self.longUrl,
        "shortUrl": self.shortUrl
    }

