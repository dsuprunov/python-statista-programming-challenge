#!/usr/bin/env python

import logging
from sqlalchemy import create_engine

import config
from models import Base


def main():
    logging.basicConfig(
        format='%(asctime)s %(levelname)s: %(message)s',
        level=logging.INFO,
        # level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logging.info(f'Creating new engine: create_engine(...)')
    engine = create_engine(
        url=config.SQLALCHEMY_URL,
        echo=config.SQLALCHEMY_ECHO
    )

    logging.info(f'Creating database and tables: Base.metadata.create_all(...)')
    Base.metadata.create_all(bind=engine)

    logging.info(f"All done")


if __name__ == '__main__':
    main()
