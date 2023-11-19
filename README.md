## Statista Programming Challenge

[![tests](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml)
[![docker build](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml)


## ToDo

- Bonus task
- Task #3
- Task 5 Include appropriate documentation in a readme.md

## Table of Contents

- [Task 1: Ingesting the data into a database](#task-1-ingesting-the-data-into-a-database)
- [Task 2: Data insights](#task-2-data-insights)
- [Task 3: Web Application](#task-3-web-application)
- [Task 4: Making our app distribution ready](#task-4-making-our-app-distribution-ready)
- [Task 5: Updating, testing, and documenting](#task-5-updating-testing-and-documenting)
- [Bonus task](#bonus-task)

---

## Task 1: Ingesting the data into a database

- ### Preparation for the next two steps

  For the next two steps, performed on your local Linux PC, create a
  virtual environment, activate it, and pre-install all packages listed in the `requirements.txt` file.
  
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
  By default (without environmental parameters), a local SQLite database `./data/census.db.sqlite3` will be created
  from a local CSV file `./data/Input_Dataset.csv`.
  <br/>
  <br/>
  If you prefer to use PostgreSQL and/or change the location of the input CSV file, please check the
  `.env` file, and remember to import it into the current environment before running the script(s).  
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

```bash
./statista-challenge-app.sh {start|init|help|stop|restart|build|test}
```
Commands:
-  **start**   - Starts the containers in the background and leaves them running
-  **init**    - Populates own/containerized PostgreSQL database with data from CSV file
-  **help**    - Displays this help message
-  **stop**    - Stops running containers without removing them
-  **restart** - Restarts all stopped and running service
-  **build**   - Builds the local docker container(s)
-  **test**    - Tests the connection to the production database and uploads scripts

## Bonus task
