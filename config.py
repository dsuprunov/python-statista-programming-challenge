import logging

#
# SQLALCHEMY
#
SQLALCHEMY_URL = 'sqlite:///./census.db.sqlite3'
# SQLALCHEMY_URL = 'sqlite:///./test.db.sqlite3'
# SQLALCHEMY_URL = 'postgresql://statista:secret@localhost:5432/statista'
SQLALCHEMY_ECHO = False

#
# csv datase file
#
CSV_FILE = './docs/Input_Dataset.csv'

#
#
#
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
