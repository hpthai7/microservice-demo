#!/bin/bash
cd ..
docker build -f build/user-service/Dockerfile -t user-service .
docker build -f build/talk-service/Dockerfile -t talk-service .

cd build
docker-compose up -d