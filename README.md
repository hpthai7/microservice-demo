# Installation
- Docker
- Docker-compose
- Linux, or WSL, or replace bash scripts in build/ with Windows scripts

# Build
```bash
cd build
bash -x build.sh
```

# Test


# Troubleshooting

```bash
# Deploy one service in multiservice docker-compose.yaml
docker-compose up -d database

# Delete service container AND remove volume
docker-compose down database -v

# Connect to dockerized Mongo from localhost needs port:
mongo -u test localhost:27017

# POST json to service using cUrl
curl -d '{"name":"Thien", "username": "thien_math"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users

curl -d '{"talk_id":"mathematics_101", "title": "Mathematics for Beginner"}' -H "Content-Type: application/json" -X POST http://localhost:5001/talks

curl -d '{"name":"Thien", "username": "thien_math"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users/thien_math/talk/mathematics_101
```
