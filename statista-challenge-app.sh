#!/bin/bash

GITHUB_REPO_URL="https://github.com/dsuprunov/python-statista-programming-challenge.git"

case "$1" in
  "help")
    echo ""
    echo "Usage: $0 {pull|start|init|help|stop|restart|build|test}"
    echo ""
    echo "  pull    - Pull the latest code from a GitHub repository"
    echo "  start   - Create and starts the containers in the background and leaves them running"
    echo "  init    - Populates own/containerized PostgreSQL database with data from CSV file"
    echo "  help    - Displays this help message"
    echo "  stop    - Stops running containers without removing them"
    echo "  restart - Restarts all stopped and running containers"
    echo "  build   - Build or rebuild services"
    echo "  test    - Tests the connection to the production database and uploads scripts"
    echo ""
    ;;

  "start")
    echo "Starting containers in the background and leaving them running..."
    docker-compose up -d --remove-orphans
    ;;

  "init")
    echo "Populating the containerized PostgreSQL database with data from a CSV file..."
    docker exec -ti $(docker ps -a -q --filter="ancestor=statista-challenge-app" --filter="status=running") /app/db_create_import.sh
    ;;

  "restart")
    echo "Restarting all stopped and running services..."
    docker-compose restart
    ;;

  "stop")
    echo "Stopping running containers without removing them..."
    docker-compose stop
    ;;

  "build")
    echo "Building containers..."
    docker-compose build
    ;;

  "test")
    echo "Testing the connection to the production database and uploads scripts..."
    docker exec -ti $(docker ps -a -q --filter="ancestor=statista-challenge-app" --filter="status=running") /app/db_test.py
    ;;

  "pull")
    echo "Pulling the latest code from a GitHub repository $GITHUB_REPO_URL"

    # check for git client
    if ! command -v git &> /dev/null; then
      echo "Git is not installed. Please install Git and try again."
      exit 1
    fi

    # clone or pull
    if [ -d "./.git" ]; then
      git pull
    else
      git clone "$GITHUB_REPO_URL"
    fi
    ;;
  *)
    echo ""
    echo "Unknown command. Use '$0 help' for usage."
    echo ""
    ;;
esac