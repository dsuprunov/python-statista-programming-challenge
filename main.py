from __future__ import annotations

import logging

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

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///census.db.sqlite3'  # config.SQLALCHEMY_URL

db = SQLAlchemy(app, model_class=Base)

with app.app_context():
    db.create_all()

@app.route('/test')
def test():
    return render_template('test.html')


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
        df = pd.read_sql_table(table_name, db.session.connection(), index_col=['id'])

        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        logging.error(e)
        return jsonify(pd.DataFrame({}).to_dict(orient='records'))


if __name__ == '__main__':
    app.run(debug=True)
