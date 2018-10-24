#!/bin/bash

# Set environment variables from .env file
set -a
[ -f .env ] && source .env
set +a

# Launch flask server
flask run
