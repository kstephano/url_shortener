from flask import request, jsonify, render_template, redirect, abort
from app import app
from controllers import paths

import string
import random

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', url_short = '')
    else:
        #generate a random string
        s = 5
        rand = "".join(random.choices(string.ascii_uppercase + string.digits, k=s))
        #map string to original link in db
        longUrl = request.form['url']
        data = {
            "longUrl": longUrl,
            "shortUrl": rand
        }
        new_url, statusCode = paths.create(data)
        print(new_url)
        return render_template('home.html', url_short = f'localhost:5000/{rand}') 

@app.route('/<short>', methods = ['GET'])
def redirect_url(short):
    #go into database -> get original link
    obj, statusCode = paths.show(short)
    print(obj, statusCode)
    if obj:
        return redirect(obj['longUrl'])
    else:
        return redirect('localhost:5000/')

@app.route('/all', methods=['GET'])
def all():
    allUrls = paths.index()
    return jsonify(allUrls)