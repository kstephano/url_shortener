from models.Path import Path, serialize

def index():
    urls = Path.all()
    return urls, 200

def show(shortUrl):
    return serialize(Path.findByShortUrl(shortUrl)), 200

def create(data):
    new_url = Path.create(longUrl=data['longUrl'], shortUrl=data['shortUrl'])
    return new_url, 201