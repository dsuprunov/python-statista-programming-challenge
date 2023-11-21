#!/usr/bin/env python

from __future__ import annotations

import os
from io import StringIO
from io import BytesIO
import base64
import logging
from flask import Response
from sqlalchemy import inspect
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

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
        df = df.head(100)

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


@app.route('/visualize', methods=['POST'])
def visualize_get():
    try:
        js_data = request.get_json()
        table_name = js_data['table']
        xAxis = js_data['xAxis']
        yAxis = js_data['yAxis']

        #
        # for 'the' main dataset instead of complicated
        # SQL query we will use view that was created before
        #
        if table_name == 'unit':
            table_name = 'view_census_data_as_csv'
        df = pd.read_sql_table(table_name, db.session.connection(), index_col=['id'])

        df = df.groupby([xAxis, yAxis]).size().reset_index(name='count')

        df = df.pivot(index=xAxis, columns=yAxis, values='count').fillna(0)
        ax = df.plot(kind='bar', stacked=True)
        # for container in ax.containers:
        #     ax.bar_label(container, fmt='%d', label_type='edge')

        plt.xlabel(f'{xAxis}')
        plt.ylabel('Count of occurrences')
        plt.title(f'Count of occurrences for each combination of `{xAxis}` and `{yAxis}` values')

        image_stream = BytesIO()
        plt.savefig(image_stream, format='png')
        image_stream.seek(0)
        plt.close()

        image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

        return jsonify({'image_base64': image_base64})
    except Exception as e:
        logging.error(e)
        return jsonify(error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True, port=8181)
