#!/usr/bin/env python

import logging

from core.helpers import DatabaseHelper
from core.helpers import LoggingHelper
from core.models import Base

import config


def main():
    LoggingHelper.set_logging_options()

    logging.info(f'Connecting to {config.SQLALCHEMY_URL}')
    db_helper = DatabaseHelper()

    logging.info(f'Creating table(s)')
    Base.metadata.create_all(bind=db_helper.engine)

    logging.info(f"All done")


if __name__ == '__main__':
    main()
