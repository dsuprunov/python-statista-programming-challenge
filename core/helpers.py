import logging
from sqlalchemy import create_engine

import config


class DatabaseHelper:
    def __init__(self):
        self.engine = create_engine(
            url=config.SQLALCHEMY_URL,
            echo=config.SQLALCHEMY_ECHO
        )

    @staticmethod
    def get_or_create(session, model, defaults=None, **kwargs):
        instance = session.query(model).filter_by(**kwargs).one_or_none()
        if instance:
            return instance
        else:
            kwargs |= defaults or {}
            instance = model(**kwargs)
            try:
                session.add(instance)
                session.commit()
            except Exception:
                session.rollback()
                instance = session.query(model).filter_by(**kwargs).one()
                return instance
            else:
                return instance

class LoggingHelper:
    @staticmethod
    def set_logging_options():
        logging.basicConfig(
            format='%(asctime)s %(levelname)s: %(message)s',
            level=logging.INFO,
            # level=logging.DEBUG,
            datefmt='%Y-%m-%d %H:%M:%S'
        )
