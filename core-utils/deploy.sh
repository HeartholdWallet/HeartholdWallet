#!/bin/bash
echo "Deploying HeartholdWallet..."
docker-compose down
docker-compose build
docker-compose up -d
echo "Deployment complete."
