import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import string
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

class Url_Shortner(db.Model):
    __tablename__ = 'url_shortners'
    id = db.Column("id", db.Integer, primary_key=True)
    long_url = db.Column("Long", db.Text)
    short_url = db.Column("Short", db.Text)

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url

    def __repr__(self):
        return "Long Url - {} and Short Url - http://127.0.0.1:5000/{}".format(self.long_url, self.short_url)


def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters = random.choice(letters)
        rand_letters = "".join(rand_letters)
        short_url = Url_Shortner.query.filter_by(short_url=rand_letters).first()
        if not short_url:
            return rand_letters



@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form['long_url']
        found_urls = Url_Shortner.query.filter_by(long_url=url).first()
        if found_urls:
            return redirect(url_for('display_short_url', url=found_urls.short_url))
        else:
            short_url = shorten_url()
            new_url = Url_Shortner(long_url = url, short_url = short_url)
            db.session.add(new_url)
            db.session.commit()
            return redirect(url_for('display_short_url', url = short_url))

    return render_template('index.html')

@app.route('/display_all')
def display_all():
    all_urls = Url_Shortner.query.all()
    return render_template('display_all.html', all_urls = all_urls)

@app.route('/display/<url>')
def display_short_url(url):
    return render_template('short.html', short_url = url)

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = Url_Shortner.query.filter_by(short_url=short_url).first()
    return redirect(long_url.long_url)

if __name__ == "__main__":
    app.run(debug=True)