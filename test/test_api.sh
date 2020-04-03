#!/bin/bash
printf "\nCreate username thi_math, having name Thi...\n"
curl -d '{"name":"Thi", "username": "thi_math"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users

printf "\nCreate username thien_math, having name Thien...\n"
curl -d '{"name":"Thien", "username": "thien_math"}' -H "Content-Type: application/json" -X POST http://localhost:5000/users

printf "\nGet all users...\n"
curl http://localhost:5000/users

printf "\nGet user thien_math...\n"
curl http://localhost:5000/users/thien_math

printf "\nCreate channel physics_101...\n"
curl -d '{"channel_id":"physics_101", "title": "Physics for Everyone"}' -H "Content-Type: application/json" -X POST http://localhost:5001/channels

printf "\nCreate channel mathematics_101...\n"
curl -d '{"channel_id":"mathematics_101", "title": "Mathematics for Beginner"}' -H "Content-Type: application/json" -X POST http://localhost:5001/channels

printf "\nGet all channels...\n"
curl http://localhost:5000/channels

printf "\nGet channel mathematics_101...\n"
curl http://localhost:5000/channels/mathematics_101

printf "\nJoin user thien_math to channel mathematics_101...\n"
curl -H "Content-Type: application/json" -X POST http://localhost:5000/users/thien_math/channel/mathematics_101

printf "\n"