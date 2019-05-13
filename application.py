'''
in anaconda terminal
$ set FLASK_APP=application.py
$ set FLASK_DEBUG=1
$ python -m flask run
'''
from flask import Flask, session,render_template,request,url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)


# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

DB_URL = "postgres://vohbopvbgbukep:8ba34e39e860c4ec52c77baa9925f8dd2c7fd64e69"
DB_URL += "a636fb35b2a94633219523@ec2-54-163-226-238.compute-1.amazonaws.com:"
DB_URL += "5432/d489mplbq8r86t"

# Set up database
engine = create_engine(DB_URL)
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    print(session)
    return render_template('front.html')
