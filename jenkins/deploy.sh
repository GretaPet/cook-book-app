#!/bin/bash

echo "Deployment stage"

scp docker-compose.yaml jenkins@swarm-manager/home/jenkins/docker-compose.yaml
ssh jenkins@swarm-manager docker stack deploy --compose-file docker-compose.yaml cook-book-app \
  DOCKER_HUB_CREDS_USR=$DOCKER_HUB_CREDS_USR \
  docker stack deploy --compose-file docker-compose.yaml cook-book-app
