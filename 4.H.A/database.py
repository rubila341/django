from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

connection_string = "mysql+pymysql://ich1:ich1_password_ilovedbs@mysql.itcareerhub.de/310524ptm_rubila341"

engine = create_engine(connection_string, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def create_tables():
    Base.metadata.create_all(engine)

def get_session():
    return session
