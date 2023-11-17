#!/usr/bin/env python

import logging
import pandas as pd
import numpy as np
import timeit
from sqlalchemy.orm import Session

from core.helpers import DatabaseHelper
from core.helpers import LoggingHelper
from core.models import Unit
from core.models import Country
from core.models import Education
from core.models import FamilyRelationship
from core.models import Gender
from core.models import Income
from core.models import MaritalStatus
from core.models import Occupation
from core.models import Race
from core.models import WorkingClass

import config


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


def main():
    LoggingHelper.set_logging_options()

    try:
        logging.info(f'Loading {config.CSV_FILE}')
        df = pd.read_csv(config.CSV_FILE)
        # df = df.head(5)
        df.replace('?', np.nan, inplace=True)
        logging.info(f'{len(df)} row(s) loaded')

        logging.info(f'Starting DatabaseHelper')
        db_helper = DatabaseHelper()

        logging.info(f'Creating new session')
        with Session(db_helper.engine) as session:
            start = timeit.default_timer()
            logging.info(f'Importing ...')
            for _, row in df.iterrows():
                """
                Expected structure
                ----
                 age                               25
                 workclass                    Private
                 fnlwgt                        226802
                 education                       11th
                 educational-num                    7
                 marital-status         Never-married
                 occupation         Machine-op-inspct
                 relationship               Own-child
                 race                           Black
                 gender                          Male
                 capital-gain                       0
                 capital-loss                       0
                 hours-per-week                    40
                 native-country         United-States
                 income                         <=50K
                """

                # TODO: This piece of code needs to be reviewed and rewritten
                unit = Unit(
                    age=(
                        None if pd.isna(row['age'])
                        else int(row['age'])
                    ),
                    working_class=(
                        None if pd.isna(row['workclass'])
                        else get_or_create(session, WorkingClass, working_class=row['workclass'])
                    ),
                    final_weight=(
                        None if pd.isna(row['fnlwgt'])
                        else int(row['fnlwgt'])),
                    # TODO: Warning! We are not checking fof NaN (but we should)
                    education=(
                        get_or_create(session, Education, education=row['education'], years=row['educational-num'])
                    ),
                    marital_status=(
                        None if pd.isna(row['marital-status'])
                        else get_or_create(session, MaritalStatus, marital_status=row['marital-status'])
                    ),
                    occupation=(
                        None if pd.isna(row['occupation'])
                        else get_or_create(session, Occupation, occupation=row['occupation'])
                    ),
                    family_relationship=(
                        None if pd.isna(row['relationship'])
                        else get_or_create(session, FamilyRelationship, family_relationship=row['relationship'])
                    ),
                    race=(
                        None if pd.isna(row['race'])
                        else get_or_create(session, Race, race=row['race'])
                    ),
                    gender=(
                        None if pd.isna(row['gender'])
                        else get_or_create(session, Gender, gender=row['gender'])
                    ),
                    capital_gain=(
                        None if pd.isna(row['capital-gain'])
                        else int(row['capital-gain'])),
                    capital_loss=(
                        None if pd.isna(row['capital-loss'])
                        else int(row['capital-loss'])),
                    hours_per_week=(
                        None if pd.isna(row['hours-per-week'])
                        else int(row['hours-per-week'])),
                    native_country=(
                        None if pd.isna(row['native-country'])
                        else get_or_create(session, Country, country=row['native-country'])
                    ),
                    income=(
                        None if pd.isna(row['income'])
                        else get_or_create(session, Income, income=row['income'])
                    ),
                )
                session.add(unit)
                session.commit()

        stop = timeit.default_timer()

        logging.info(f'Imported {len(df)} row(s) in {stop - start} second(s)')
        logging.info(f'All done')
    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    main()
