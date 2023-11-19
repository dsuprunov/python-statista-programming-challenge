#!/usr/bin/env python

import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from sqlalchemy.engine import URL

from core.helpers import DatabaseHelper
from core.helpers import LoggingHelper
from db_create import db_create
from db_import import db_import

import config


def main():
    try:
        LoggingHelper.set_logging_options()

        logging.info(f'Testing connection to the production database {config.SQLALCHEMY_URL}')
        db_helper = DatabaseHelper()
        try:
            with Session(db_helper.engine) as session:
                assert session is not None
        except OperationalError as e:
            logging.error(f'Production database connection test failed: {e}')
        logging.info('Production database connection test OK')

        logging.info(f'Creating SQLAlchemy test engine')
        test_engine = create_engine(
            url=URL.create(drivername='sqlite', database=':memory:'),
            echo=False
        )
        logging.info(f'SQLAlchemy engine: {test_engine}')

        logging.info(f'Testing the creation of a database schema.')
        db_create(test_engine)
        logging.info(f'Schema creation: OK')

        num_of_rows = 100
        logging.info(f'Testing CSV data import (first {num_of_rows} rows)')
        db_import(test_engine, num_of_rows)
        logging.info(f'Data import: OK')

        logging.info(f'All done')
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()
