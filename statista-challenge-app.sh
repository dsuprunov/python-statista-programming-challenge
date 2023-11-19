#!/bin/bash

case "$1" in
  "help")
    echo ""
    echo "Usage: $0 {start|init|help|stop|restart|build|test}"
    echo ""
    echo "  start   - Starts the containers in the background and leaves them running"
    echo "  init    - Populates own/containerized PostgreSQL database with data from CSV file"
    echo "  help    - Displays this help message"
    echo "  stop    - Stops running containers without removing them"
    echo "  restart - Restarts all stopped and running service"
    echo "  build   - Builds the local docker container(s)."
    echo "  test    - Tests the upload scripts and connection to the database"
    echo ""
    ;;

  "start")
    echo "Starting containers in the background and leaving them running..."
    docker-compose up -d --remove-orphans
    ;;

  "init")
    echo "Populating the containerized PostgreSQL database with data from a CSV file..."
    docker exec -ti $(docker ps -a -q --filter="ancestor=statista-challenge-app" --filter="status=running") /app/db_create_import.sh 100
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
    echo "Testing..."
#    docker-compose build
    ;;
  *)
    echo ""
    echo "Unknown command. Use '$0 help' for usage."
    echo ""
    ;;
esac