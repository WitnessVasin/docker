# Остановка и удаление контейнеров

1. docker stop $(docker ps -a -q) - остановка всех контейнеров

2. docker rm $(docker ps -a -q) - удаляем все контейнеры 

3. docker rmi $(docker images -q) - удаляем все образы 