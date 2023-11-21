## Statista Programming Challenge

[![tests](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/tests.yml)
[![docker build](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml/badge.svg)](https://github.com/dsuprunov/python-statista-programming-challenge/actions/workflows/docker.yml)

## Table of Contents

- [Task 1: Ingesting the data into a database](#task-1-ingesting-the-data-into-a-database)
- [Task 2: Data insights](#task-2-data-insights)
- [Task 3: Web Application](#task-3-web-application)
- [Task 4: Making our app distribution ready](#task-4-making-our-app-distribution-ready)
- [Task 5: Updating, testing, and documenting](#task-5-updating-testing-and-documenting)
- [Bonus task](#bonus-task)

If you are a Data Engineer or a DevOps Engineer, you can proceed directly
to the [Task 5: Updating, testing, and documenting](#task-5-updating-testing-and-documenting) to review the instructions
for launching the application and fulfilling all the infrastructure requirements.

---

## Task 1: Ingesting the data into a database

- ### Preparation for the next two steps

  The project was developed using **Python** version `3.10.12` and additionally tested in version `3.12.0`

  For the next two steps, performed on your local Linux PC, create a
  virtual environment, activate it, and pre-install all packages listed in the `requirements.txt` file.
  
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
  By default (without environmental parameters), a local SQLite database `./instance/census.db.sqlite3` will be created
  from a local CSV file `./data/Input_Dataset.csv`.
  <br/>
  <br/>
  If you prefer to use PostgreSQL and/or change the location of the input CSV file, please check the
  `.docker.env` file, and remember to import it into the current environment before running the script(s).  
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
  I added [Jupyter Notebook as PDF](docs/task_20.pdf) because sometimes my local instance of Jupyter Notebook does
  not display it correctly. 
- ### Subtask: [JSON with questions and answers](docs/task_24.json)

## Task 3: Web Application

- ### at local Linux PC
  Start the web application
  ```bash
  ./main.py
  ```
  The application will be accessible at [http://localhost:8181](http://localhost:8181)

- ### as dockerized service
  - Make sure to complete all the steps outlined in [Task 5: Updating, testing, and documenting](#task-5-updating-testing-and-documenting)
  - The application will be accessible at `http://-YOUR-DOCKER-PC-ADDRESS-OR-NAME-:8181`

- ### You can find 'all data', dynamically joined into one table (in a format similar to the original CSV), in the `unit` table.
  
- ### For graphical visualizations, I discovered several appealing charts related to the 'unit' table.
  - Age vs Workclass
  - Gender vs Workclass
  - Age vs Income
  - etc


## Task 4: Making our app distribution ready

- ### Subtask: [Dockerfile](Dockerfile)
- ### Subtask: [Docker compose file](docker-compose.yml)

## Task 5: Updating, testing, and documenting

### Comments

The entire process is built around the `./data/Input_Dataset.csv` file. Under normal circumstances,
it is a part of the `statista-challenge-app:latest` image. If you want to work with your own dataset,
ensuring it follows the same format and structure, you have two options:

1. Replace `./data/Input_Dataset.csv` with your file and rebuild the Docker image. \
   You will need to restart the docker-compose service named `statista-challenge-app`.
2. Alternatively, you can mount `./data/` into your container. \
   This will allow you to change the content of the `./data/Input_Dataset.csv` without
   the need to rebuild and restart the service.
   <br/>
   <br/>
   Please uncomment the relevant code in `docker-compose.yml`
   ```yaml
   #    volumes:
   #      - ./data/:/app/data
   ```
   But, once again, you will need to restart the docker-compose service `statista-challenge-app`.
 
By default (without environmental parameters), a local (inside of `statista-challenge-app` container)
SQLite database `/app/instance/census.db.sqlite3` will be created from a local (again inside of `statista-challenge-app`
container) CSV file `/app/data/Input_Dataset.csv`.
<br/>
<br/>
If you prefer to use your own PostgreSQL server, please check the `.docker.env` file.
The values in it will be automatically imported and used inside the containers. 

### Typical workflow
1. **This step is necessary only if you have not downloaded and run this project before.** \
  Download [statista-challenge-app.sh](statista-challenge-app.sh) if it has not been downloaded yet.   
   ```bash
   wget https://raw.githubusercontent.com/dsuprunov/python-statista-programming-challenge/main/statista-challenge-app.sh
   chmod 755 statista-challenge-app.sh
   ./statista-challenge-app.sh pull 
   rm statista-challenge-app.sh
   cd python-statista-programming-challenge
   ```
   The other option is to simply clone the GitHub repository. \
   You need to have the Git client installed.
   ```bash
   git clone https://github.com/dsuprunov/python-statista-programming-challenge.git
   cd python-statista-programming-challenge
   ```
2. Pull the latest code from GitHub repo
   ```bash
   ./statista-challenge-app.sh pull
   ```
3. Build an image
   ```bash
   ./statista-challenge-app.sh build
   ```
4. Start the services
   ```bash
   ./statista-challenge-app.sh start
   ```
5. Test database connection and import script
   ```bash
   ./statista-challenge-app.sh test
   ```
6. Import data from CSV file
   ```bash
   ./statista-challenge-app.sh init
   ```
7. Do something...
   ```
   # For example, work with data or the database.
   ```
8. Stop services (if you do not need them)
   ```bash
   ./statista-challenge-app.sh stop
   ```
   
### General usage
```bash
./statista-challenge-app.sh {pull|start|init|help|stop|restart|build|test}
```
Commands:
- **pull**     - Pull the latest code from a GitHub repository
-  **start**   - Create and starts the containers in the background and leaves them running
-  **init**    - Populates own/containerized PostgreSQL database with data from CSV file
-  **help**    - Displays this help message
-  **stop**    - Stops running containers without removing them
-  **restart** - Restarts all stopped and running containers
-  **build**   - Build or rebuild services
-  **test**    - Tests the connection to the production database and uploads scripts

## Bonus task

The bonus task, unfortunately, was not completed because I decided to invest my time
in completing all the primary tasks, bringing the code into compliance with PEP8 standards
(with a few exceptions, such as docstrings), formatting the documentation to a more
readable state, and releasing a new version. Additionally, time was spent searching
for a more optimal way to import a CSV file into the database. Two additional solutions
were found (caching and bulk upload directly through the database), the implementation
of which was beyond the scope of this assignment.