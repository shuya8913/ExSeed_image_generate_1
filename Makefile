all: build up exec

build:
	docker compose  build 

up:
	docker compose up -d

down:
	docker compose down

exec:
	docker compose exec exseed_demo /bin/bash