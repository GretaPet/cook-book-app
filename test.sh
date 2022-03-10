#!/bin/bash

source venv/Scripts/activate
pythom -m pytest \
  --cov
  --cov=application
  --cov-report term-missing
  --cov-report xml:coverage.xml
  --junitxml=junit_report.xml
