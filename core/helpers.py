import logging
from sqlalchemy import create_engine

import config


class DatabaseHelper:
    def __init__(self):
        self.engine = create_engine(
            url=config.SQLALCHEMY_URL,
            echo=config.SQLALCHEMY_ECHO
        )

class LoggingHelper:
    @staticmethod
    def set_logging_options():
        logging.basicConfig(
            format='%(asctime)s %(levelname)s: %(message)s',
            level=logging.INFO,
            # level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S'
        )
