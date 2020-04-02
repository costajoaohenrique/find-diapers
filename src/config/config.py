from os import environ

from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_SERVER = environ.get('DB_SERVER')
    DB_USER_NAME= environ.get('DB_USER_NAME')
    DB_USER_PASSWORD = environ.get('DB_USER_PASSWORD')
    DB_NAME = environ.get('DB_NAME')


