#!/bin/bash

echo "This is test stage"

python3 -m venv venv
source venv/bin/activate

pip3 install pytest pytest-cov flask_testing
pip3 install -r requirements.txt

python3 -m pytest application \
  --cov=application \
  --cov-report term-missing \
  --cov-report xml:test_files/coverage.xml \
  --junitxml=test_files/junit_report.xml

deactivate
rm -rf venv
