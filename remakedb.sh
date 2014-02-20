#!/bin/bash

dropdb playful_geometer_db
createdb playful_geometer_db
./manage.py syncdb
python populate_database.py

