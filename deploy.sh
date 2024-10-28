#!/bin/bash

# deactivate old venv if active
if [ -d "venv" ]; then
    # Check if the virtual environment is active
    if [[ "$VIRTUAL_ENV" != "" ]]; then
        deactivate
    fi
    
    # delete old venv
    echo "Deleting old virtual environment..."
    rm -rf venv
fi

# create new venv
echo "Creating new virtual environment..."
python -m venv venv

# activate new venv
echo "Activating virtual environment..."
source venv/bin/activate

# install requirements
echo "Installing requirements..."
pip install --upgrade pip  # Upgrade pip to the latest version
pip install -r requirements.txt

# Run the app with Uvicorn
echo "Running the app with Uvicorn..."
python run_uvicorn.py
