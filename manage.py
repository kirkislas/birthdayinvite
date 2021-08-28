import os
from flask import Flask, redirect, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

db = SQLAlchemy(app)


class Guest(db.Model):
    __tablename__ = 'guests'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(25),unique=True)
    numOfGuests=db.Column(db.Integer,nullable=False)

    def __init__(self,name,numOfGuests):
        self.name=name
        self.numOfGuests=numOfGuests
       


@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/#section2", methods=['GET'])
def rsvp():
    return render_template("index.html")


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        numOfGuests=request.form['number-input']

        guest=Guest(name,numOfGuests)
        db.session.add(guest)
        db.session.commit()

    if request.method == 'GET':
        guestResult=db.session.query(Guest).filter(Guest.id==1)
        for result in guestResult:
            print(result.name)
    return render_template("success.html",data=name)




if __name__ == "__main__":
    app.run(debug=True)