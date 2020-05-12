#!/bin/bash

# make sure we execute script from the server/ directory
cd -P -- "$(dirname -- "$0")" 

docker network create --driver bridge notification-network
docker rm -f notification-server
powershell.exe 'docker run -d --name notification-server -p 9998:80 -v "$(pwd):/app" --network notification-network tiangolo/uvicorn-gunicorn-fastapi:python3.7'
