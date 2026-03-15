import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Security key for Flask sessions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Azure Storage Blob Settings
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'cmsstorage123'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'

    # Azure SQL Database Settings
    SQL_SERVER = os.environ.get('SQL_SERVER') or 'cms-server12.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'cms-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')
    
    # Construct the Connection String
    # Note: Azure App Service Linux uses 'ODBC Driver 17 for SQL Server' or 'ODBC Driver 18 for SQL Server'
    if SQL_USER_NAME and SQL_PASSWORD:
        SQLALCHEMY_DATABASE_URI = (
            f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/{SQL_DATABASE}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        )
    else:
        # Fallback to local SQLite if environment variables are missing
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### MS Authentication (Optional / Future Use) ###
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    AUTHORITY = "https://login.microsoftonline.com"
    CLIENT_ID = os.environ.get("CLIENT_ID")
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
