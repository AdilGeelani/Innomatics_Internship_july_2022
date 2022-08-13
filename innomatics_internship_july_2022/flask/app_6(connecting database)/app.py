import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


############################SQL Alchemy Configuration#########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# pass application config to SQLAlchemy instance
db = SQLAlchemy(app)
# Migrate is a tool for database migrations
# Migrate will take application config and a db instance and upgrade the database
Migrate(app, db)

#############################################################################################
############################Create a Model###################################################

class Sabji(db.Model):
    __tablename__ = 'sabjis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    mrp = db.Column(db.Integer)
    
    def __int__(self, name, mrp):
        self.name = name
        self.mrp = mrp
    def __repr__(self):
        return "Sabji Name - {} and MRP - {}".format(self.name, self.mrp)


#############################################################################################
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form['in_1']
        mrp = request.form['in_2']
        new_sabji = Sabji(name=name, mrp=mrp)
        db.session.add(new_sabji)
        db.session.commit()
    return render_template('add.html')

@app.route('/search')
def search():
    name = request.args.get('in_1')
    sabji = Sabji.query.filter_by(name=name).first()
    sabjis = Sabji.query.all()
    return render_template('search.html', sabji = sabji, sabjis = sabjis)

@app.route('/display')
def display_all():
    sabjis = Sabji.query.all()
    return render_template('display.html', sabjis = sabjis)



if __name__ == '__main__':
    app.run(debug=True)