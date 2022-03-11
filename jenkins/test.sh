#!/bin/bash

echo "This is test stage"

python3 -m venv venv
source venv/bin/activate

pip3 install pytest pytest-cov flask_testing
pip3 install -r requirements.txt

mkdir test_files

python3 -m pytest application \
  --cov=application \
  --cov-report term-missing \
  --cov-report xml:test_filles/coverage.xml \
  --junitxml=test_filles/junit_report.xml

deactivate
rm -rf venv
