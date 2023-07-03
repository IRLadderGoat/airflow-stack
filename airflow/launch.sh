#!/bin/bash

# Airflow needs a home. `~/airflow` is the default, but you can put it
# somewhere else if you prefer (optional)
export AIRFLOW_HOME=~/Documents/airflow-stack/airflow
export DBT_PROFILES_DIR=~/.dbt

# Install Airflow using the constraints file
AIRFLOW_VERSION=2.6.0
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.7
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.4.3/constraints-3.7.txt
source .venv/bin/activate
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

if [ $# -eq 0 ]; then
	airflow scheduler & airflow webserver --port 8080 && fg
elif [ "$1" == "--setup"]; then
	# The Standalone command will initialise the database, make a user,
	# and start all components for you.
	airflow standalone
else 
	echo "Invalid flag: $1"
	echo "usage: ./launch [--setup]"
	exit 1
fi

# Visit localhost:8080 in the browser and use the admin account details
# shown on the terminal to login.
