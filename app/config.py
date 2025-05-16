import os

class Config(object):
    APPNAME = "app"
    ROOT = os.path.abspath(APPNAME)
    UPLOAD_PATH = '/static/upload/'
    SERVER_PATH = ROOT + UPLOAD_PATH

    USER = os.environ.get('POSTGRES_USER', 'neondb_owner')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'npg_G7ibTD3YnpkH')
    HOST = os.environ.get('POSTGRES_HOST', 'ep-damp-cell-a2lo8071-pooler.eu-central-1.aws.neon.tech')  # Укажите localhost
    PORT = os.environ.get('POSTGRES_PORT', 5432)        # Порт 54321
    DB = os.environ.get('POSTGRES_DB', 'neondb')

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://neondb_owner:npg_G7ibTD3YnpkH@ep-damp-cell-a2lo8071-pooler.eu-central-1.aws.neon.tech/neondb?sslmode=require"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SECRET_KEY = 'hfs7d8ftgy487fgseufh893204hgr78odfb'
