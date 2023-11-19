import os
import logging
from dotenv import load_dotenv
from sqlalchemy.engine import URL


#
# Defaults
#
# The default values will be used if there are
# no such variables in the environment:
# - Postgres database settings: POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
# - SQLite database settings: SQLITE_DB_FILE
# - Input file settings: INPUT_CSV_FILE
#
DEFAULT_SQLITE_DB_FILE = './census.db.sqlite3'
DEFAULT_INPUT_CSV_FILE = './Input_Dataset.csv'

#
# Something for tests
#
# DEFAULT_SQLITE_DB_FILE = './test.db.sqlite3'
# load_dotenv()

#
# SQLAlchemy
#
SQLALCHEMY_URL = ''
SQLALCHEMY_ECHO = False

if all(e in os.environ for e in ['POSTGRES_DB', 'POSTGRES_USER', 'POSTGRES_PASSWORD']):
    SQLALCHEMY_URL = URL.create(
        drivername='postgresql',
        username=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        host='localhost',
        port='5432',
        database=os.environ['POSTGRES_DB'],
    )
elif 'SQLITE_DB_FILE' in os.environ:
    SQLALCHEMY_URL = URL.create(
        drivername='sqlite',
        database=os.environ['SQLITE_DB_FILE'],
    )
else:
    SQLALCHEMY_URL = URL.create(
        drivername='sqlite',
        database=DEFAULT_SQLITE_DB_FILE,
    )

#
# File to import
#
CSV_FILE = ''
if 'INPUT_CSV_FILE' in os.environ:
    CSV_FILE = os.environ['INPUT_CSV_FILE']
else:
    CSV_FILE = DEFAULT_INPUT_CSV_FILE


#
# Logging settings
#
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
