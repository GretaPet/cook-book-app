#!/bin/bash

echo "Deployment stage"
ssh jenkins@swarm-manager docker stack deploy --compose-file docker-compose.yaml cook-book-app
