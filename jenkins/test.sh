#!/bin/bash

echo "This is test stage"

python3 -m venv venv
source venv/bin/activate

pip3 install pytest pytest-cov flask_testing requests_mock
pip3 install -r requirements.txt

mkdir test_reports

python3 -m pytest \
  --cov \
  --cov=application \
  --cov-report term-missing \
  --cov-report xml:coverage.xml \
  --junitxml=junit_report.xml

deactivate
rm -rf venv
