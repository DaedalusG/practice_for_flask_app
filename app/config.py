import os


class Configuration:
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABSE_URL")
    SQLALCHEMY_DATABASE_URI = "postgresql://pyweb_practice_user:pyweb@localhost/pyweb_practice_db"  # noqa
    SECRET_KEY = "secret stuff"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
