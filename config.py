import os
from dotenv import load_dotenv
load_dotenv()
DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI", 'mysql+pymysql://root:thehut@localhost:3306/thehut')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'thehut'
