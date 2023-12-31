#!/usr/bin/env python

import sys
import logging
import pandas as pd
import numpy as np
import timeit
from sqlalchemy import Engine
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


def db_import(engine: Engine, num_rows_to_import: int | None = None):
    try:
        logging.info(f'Loading {config.CSV_FILE}')
        df = pd.read_csv(config.CSV_FILE)
        if num_rows_to_import is not None:
            df = df.head(num_rows_to_import)
        df.replace('?', np.nan, inplace=True)
        logging.info(f'{len(df)} row(s) loaded')

        logging.info(f'Creating new session')
        with Session(engine) as session:
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
                        else DatabaseHelper.get_or_create(session, WorkingClass, working_class=row['workclass'])
                    ),
                    final_weight=(
                        None if pd.isna(row['fnlwgt'])
                        else int(row['fnlwgt'])),
                    # TODO: Warning! We are not checking fof NaN (but we should)
                    education=(
                        DatabaseHelper.get_or_create(session, Education, education=row['education'], years=row['educational-num'])
                    ),
                    marital_status=(
                        None if pd.isna(row['marital-status'])
                        else DatabaseHelper.get_or_create(session, MaritalStatus, marital_status=row['marital-status'])
                    ),
                    occupation=(
                        None if pd.isna(row['occupation'])
                        else DatabaseHelper.get_or_create(session, Occupation, occupation=row['occupation'])
                    ),
                    family_relationship=(
                        None if pd.isna(row['relationship'])
                        else DatabaseHelper.get_or_create(session, FamilyRelationship, family_relationship=row['relationship'])
                    ),
                    race=(
                        None if pd.isna(row['race'])
                        else DatabaseHelper.get_or_create(session, Race, race=row['race'])
                    ),
                    gender=(
                        None if pd.isna(row['gender'])
                        else DatabaseHelper.get_or_create(session, Gender, gender=row['gender'])
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
                        else DatabaseHelper.get_or_create(session, Country, country=row['native-country'])
                    ),
                    income=(
                        None if pd.isna(row['income'])
                        else DatabaseHelper.get_or_create(session, Income, income=row['income'])
                    ),
                )
                session.add(unit)
                session.commit()

        stop = timeit.default_timer()
        logging.info(f'Imported {len(df)} row(s) in {stop - start} second(s)')

    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    LoggingHelper.set_logging_options()

    limit = None
    try:
        limit = int(sys.argv[1])
    except:
        pass

    logging.info(f'Connecting to {config.SQLALCHEMY_URL}')
    db_helper = DatabaseHelper()

    db_import(db_helper.engine, limit)

    logging.info(f'All done')
