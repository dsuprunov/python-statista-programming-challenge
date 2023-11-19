#!/bin/bash

python db_create.py && python db_import.py "$@"