#!/bin/bash

echo "This is test stage"

python3 -m venv venv
source venv/bin/activate

pip3 install pytest pytest-cov flask_testing wheel
pip3 install -r requirements.txt

python3 -m pytest \
  --cov=application \
  --cov-report term-missing \
  --cov-report xml:tests/coverage.xml \
  --junitxml=tests/junit_report.xml

deactivate
rm -rf venv
