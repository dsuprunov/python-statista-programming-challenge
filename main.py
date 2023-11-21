#!/usr/bin/env python

from __future__ import annotations

import logging
from io import StringIO
import os
import sys
from sqlalchemy.engine.url import make_url
from flask import Flask
from flask import request
from flask import jsonify
from flask import Response
from sqlalchemy import create_engine, inspect, select
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from icecream import ic
import pandas as pd
from flask import Flask, render_template, request, jsonify

from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base

import config

app = Flask(__name__, instance_path=os.getcwd())
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_URL

db = SQLAlchemy(app, model_class=Base)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    inspector = inspect(db.engine)
    data = {
        'tables': sorted(inspector.get_table_names()),
    }

    return render_template('index.html', data=data)


@app.route('/table/<string:table_name>', methods=['GET'])
def table_get(table_name):
    try:
        #
        # for 'the' main dataset instead of complicated
        # SQL query we will use view that was created before
        #
        if table_name == 'unit':
            table_name = 'view_census_data_as_csv'
        df = pd.read_sql_table(table_name, db.session.connection(), index_col=['id'])

        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        logging.error(e)
        return jsonify(pd.DataFrame({}).to_dict(orient='records'))


@app.route('/data', methods=['POST'])
def data_get():
    try:
        js_data = request.get_json()
        table_name = js_data['table']
        fields = js_data['fields']

        #
        # for 'the' main dataset instead of complicated
        # SQL query we will use view that was created before
        #
        if table_name == 'unit':
            table_name = 'view_census_data_as_csv'
        df = pd.read_sql_table(table_name, db.session.connection(), index_col=['id'])
        df = df.drop(columns=set(df.columns) - set(fields))

        csv_data = StringIO()

        df.to_csv(csv_data, index=False)

        response = Response(csv_data.getvalue(), content_type='text/csv')
        response.headers['Content-Disposition'] = f'attachment; filename={table_name}_export.csv'

        return response
    except Exception as e:
        logging.error(e)
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True, port=8181)
