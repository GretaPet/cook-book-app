#!/bin/bash

echo "Deployment stage"
ssh jenkins@VM01 docker stack deploy --compose-file docker-compose.yaml cook-book-app
