#!/bin/bash

# Function to handle termination signals
shutdown() {
    echo "Shutting down..."
    # Add commands to gracefully shut down services
    kill -s SIGTERM $!
    wait $!
}

# Trap termination signals
trap shutdown SIGTERM SIGINT

# Start Jupyter Notebook with no token and no password
jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --port=8888 --NotebookApp.token='' --NotebookApp.password='' &

# Start uWSGI server
uwsgi --ini /app/uwsgi.ini &

# Wait for any process to exit
wait -n

# Capture the exit code of the process that exited
exit_code=$?

# Exit the script with the captured exit code
exit $exit_code
