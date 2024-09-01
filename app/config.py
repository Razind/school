import os

class Config(object):
    APPNAME = "app"
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('POSTGRES_USER', 'razind')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'razind')
    HOST = os.environ.get('POSTGRES_HOST', 'postgres')
    PORT = os.environ.get('POSTGRES_PORT', 5332)
    DB = os.environ.get('POSTGRES_DB', 'mydb')


    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@"
        f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    ) 
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = 'hfs7d8ftgy487fgseufh893204hgr78odfb'
