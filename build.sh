#!/bin/bash

docker-compose -f docker-compose.yml up -d --remove-orphans

# Сборка Docker образов из указанных директорий
docker build -t fineken/lab2 ./1
docker build -t fineken/data_processor ./2
docker build -t fineken/logger ./3

# Запуск приложения с помощью Docker Compose
docker-compose -f docker-compose.yml up -d
