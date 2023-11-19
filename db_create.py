#!/usr/bin/env python

import logging
from sqlalchemy import Engine

from core.helpers import DatabaseHelper
from core.helpers import LoggingHelper
from core.models import Base

import config


def db_create(engine: Engine):
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    LoggingHelper.set_logging_options()

    logging.info(f'Connecting to {config.SQLALCHEMY_URL}')
    db_helper = DatabaseHelper()

    logging.info(f'Creating table(s)')
    db_create(db_helper.engine)

    logging.info(f"All done")
