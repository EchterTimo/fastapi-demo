#!/bin/bash

# create venv
python -m venv venv

# activate venv
source venv/bin/activate

# install requirements
pip install -r requirements.txt

# Run the app with Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000
