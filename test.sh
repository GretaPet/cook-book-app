#!/bin/bash

sudo apt update
sudo apt install python python-venv python-pip
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

python create.py
python app.py
