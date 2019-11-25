from flask import Flask
from flask_cors import CORS
import redis
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
CORS(app)
cache_db = redis.Redis(host='10.10.10.10')
app.config['SECRET_KEY'] = 'trantrongtyckiuzk4ever!@#!!!@@##!*&%^$$#$'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Ckiuzk4ever!@#@10.10.10.10:5432/crmapp'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=False)
Base = declarative_base()
from Src.SqlClass import Model

Base.metadata.create_all(engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.commit()

from Src.View.View import transaction

app.register_blueprint(transaction)
