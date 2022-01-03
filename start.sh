#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn --reload restapi.restapi.wsgi:application \
    --bind 0.0.0.0:8000