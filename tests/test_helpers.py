import pytest
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from core.helpers import DatabaseHelper
from core.helpers import LoggingHelper


def test_database_helper_test_get_or_create():
    #
    # create mock scheme
    #
    class Base(DeclarativeBase):
        pass

    class Fruit(Base):
        __tablename__ = 'fruits'
        id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
        value: Mapped[str] = mapped_column(unique=True)

    #
    # use SQLite in-memory database
    #
    engine = create_engine("sqlite://")
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        for v in ['apple', 'orange', 'apple']:
            DatabaseHelper.get_or_create(session, Fruit, value=v)
            session.commit()

        statement = select(Fruit)
        counter = len(session.execute(statement).all())

        # we should have only 2 fruits in the table
        assert counter == 2

    assert True


def test_logging_helper():
    LoggingHelper.set_logging_options()

    # logger = logging.getLogger(__name__)
    # logger.info('info level')
    # logger.warning('warning level')
    # logger.error('error level')
    # logger.critical('critical level')

    assert True
