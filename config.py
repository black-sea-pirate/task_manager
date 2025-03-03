from dotenv import *
import os
load_dotenv()

class Config:
    DB_NAME= os.getenv("DB_NAME")
    DB_USER= os.getenv("DB_USER")
    DB_PASSWORD= os.getenv("DB_PASSWORD")
    DB_HOST= os.getenv("DB_HOST")
    DB_PORT= os.getenv("DB_PORT")

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False