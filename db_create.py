#!/usr/bin/env python

import logging
from sqlalchemy import Engine
from sqlalchemy import text
from sqlalchemy.orm import Session

from core.helpers import DatabaseHelper
from core.helpers import LoggingHelper
from core.models import Base

import config


def db_create(engine: Engine):

    sql_create_view = '''
        CREATE VIEW view_census_data_as_csv AS
        SELECT
            unit.id AS id,
            unit.age AS age,
            working_class.working_class AS workclass,
            unit.final_weight AS fnlwgt,
            education.education AS education,
            education.years AS "educational-num",
            marital_status.marital_status AS "marital-status",
            occupation.occupation AS occupation,
            family_relationship.family_relationship AS relationship,
            race.race AS race,
            gender.gender AS gender,
            unit.capital_gain AS "capital-gain",
            unit.capital_loss AS "capital-loss",
            unit.hours_per_week AS "hours-per-week",
            country.country AS "native-country",
            income.income AS income
        FROM
            unit
        LEFT JOIN
            country ON country.id = unit.native_country_id
        LEFT JOIN
            gender ON gender.id = unit.gender_id
        LEFT JOIN
            race ON race.id = unit.race_id
        LEFT JOIN
            occupation ON occupation.id = unit.occupation_id
        LEFT JOIN
            income ON income.id = unit.income_id
        LEFT JOIN
            family_relationship ON family_relationship.id = unit.family_relationship_id
        LEFT JOIN
            marital_status ON marital_status.id = unit.marital_status_id
        LEFT JOIN
            education ON education.id = unit.education_id
        LEFT JOIN
            working_class ON working_class.id = unit.working_class_id
        ;
    '''

    try:
        Base.metadata.create_all(bind=engine)

        with Session(engine) as session:
            session.execute(text(sql_create_view))
            session.commit()

    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    LoggingHelper.set_logging_options()

    logging.info(f'Connecting to {config.SQLALCHEMY_URL}')
    db_helper = DatabaseHelper()

    logging.info(f'Creating table(s)')
    db_create(db_helper.engine)

    logging.info(f"All done")
