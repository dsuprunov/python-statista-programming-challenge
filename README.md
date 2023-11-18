## Statista Programming Challenge

[![tests](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml)
[![docker build](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml)

---

## Table of Contents

- [Task 1: Ingesting the data into a database](#task-1-ingesting-the-data-into-a-database)
- [Task 2: Data insights](#task-2-data-insights)
- [Task 3: Web Application](#task-3-web-application)
- [Task 4: Making our app distribution ready](#task-4-making-our-app-distribution-ready)
- [Task 5: Updating, testing, and documenting](#task-5-updating,-testing,-and-documenting)

---

## Task 1: Ingesting the data into a database

- ### Normalized database schema

  - [As pdf](docs/database.pdf)
  - [As interactive view](https://dbdiagram.io/d/655516d67d8bbd6465445e36)
  - [As DML file](docs/database.dbml)

- ### Database schema creation script:

    ```console
    ~/db_create.py
    ```

- ### Database data import:

    ```console
    ~/db_import.py
    ```

## Task 2: Data insights

- ### [Jupyter Notebook](docs/task_20.ipnb)
- ### [JSON with questions and answers](docs/task_20.ipnb)

## Task 3: Web Application

## Task 4: Making our app distribution ready

## Task 5: Updating, testing, and documenting
- docker-compose up --detach
- docker-compose restart
- docker-compose stop