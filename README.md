## Statista Programming Challenge

[![tests](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml)
[![docker build](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml)


## ToDo

- Bonus task
- Task #3
- Task #5 (we need more documentation)

## Table of Contents

- [Task 1: Ingesting the data into a database](#task-1-ingesting-the-data-into-a-database)
- [Task 2: Data insights](#task-2-data-insights)
- [Task 3: Web Application](#task-3-web-application)
- [Task 4: Making our app distribution ready](#task-4-making-our-app-distribution-ready)
- [Task 5: Updating, testing, and documenting](#task-5-updating,-testing,-and-documenting)
- [Bonus task](#bonus-task)

---

## Task 1: Ingesting the data into a database

- ### Preparation for the Next Two Steps

  For the next two steps (which are performed on your local Linux PC), you need to pre-install
  all the packages listed in the `requirements.txt` file.
  
  ```bash
  pip install -r requirements.txt
  ```
  By default (without environmental parameters), a local SQLite database `census.db.sqlite3` will be created
  from a local CSV file `./Input_Dataset.csv`.
  <br/>
  <br/>
  If you prefer to use PostgreSQL and/or change the location of the input CSV file, please check the
  `.env` file, and remember to import it into the current environment before running the script.  
  <br/>
  In case you decided to use PostgreSQL, please create both the user and the database.
  <br/>  
  ```sql
  CREATE USER census WITH PASSWORD 'secret';
  CREATE DATABASE census OWNER census;
  ```


- ### Subtask: Normalized database schema

  - [As pdf](docs/dbdiagram.pdf)
  - [As interactive view](https://dbdiagram.io/d/655516d67d8bbd6465445e36)
  - [As DBML (Database Markup Language) file](docs/dbdiagram.dbml)

- ### Subtask: Database schema creation script

  ```console
  ./db_create.py
  ```

- ### Subtask: Database data import

  ```console
  ./db_import.py
  ```

## Task 2: Data insights

- ### Subtask: [Jupyter Notebook](docs/task_20.ipnb)
- ### Subtask: [JSON with questions and answers](docs/task_24.json)

## Task 3: Web Application

## Task 4: Making our app distribution ready

- ### Subtask: [Dockerfile](Dockerfile)
- ### Subtask: [Docker compose file](docker-compose.yml)

## Task 5: Updating, testing, and documenting

- Create a bash script which we can use to 
  pull code from a repository, 
  rebuild our application, 
  and run the docker compose file in the repository
- Add unit tests to test the upload scripts and connection to the SQLite and/or Postgres database 
- Include appropriate documentation in a readme.md

## Bonus task
