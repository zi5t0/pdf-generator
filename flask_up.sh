#!/bin/bash
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
flask run --host 0.0.0.0 --port 5000
