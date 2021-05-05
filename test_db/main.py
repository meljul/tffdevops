from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import requests



app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://flaskalk:123456a.@db/flaskalk_db' #Type db, user, mdp @ serveur db / nom db
CORS(app)


db = SQLAlchemy(app)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    operation = db.Column(db.String(200))
    date = db.Column(db.DateTime)

    

@app.route('/')
def index():
    historique = History.query.order_by(History.date.desc()).first()

    return "Dernier resultat : {}".format(historique.operation)

@app.route('/add/<int:add1>/<int:add2>')
def add(add1, add2):
    newOperation = "{} + {} = {}".format(add1, add2, add1 + add2)
    historyLine = History(operation=newOperation, date=datetime.now())

    db.session.add(historyLine)
    db.session.commit()

    return "Operation {} realisée a la date {}.".format(newOperation, datetime.now())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
