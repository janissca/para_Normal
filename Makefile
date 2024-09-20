.DEFAULT_GOAL := build

.PHONY:fmt vet build

build:
	docker-compose up

build_backend:
	cd backend && docker build -t my_django_app . 
	docker run --name backend -p 8000:8000 my_django_app
	@echo "server opened on http://localhost:8000/api/v1"

build_frontend:

	cd frontend && docker build -t my_frontend_app .
	docker run --name frontend -p 3000:3000 my_frontend_app
	@echo "server opened on http://localhost:3000"

clear_backend:
	docker stop backend
	docker remove backend
	docker rmi my_django_app

clear_frontend:
	docker stop frontend
	docker remove frontend
	docker rmi my_frontend_app

clear_all: clear_backend clear_frontend

delete_all:
	docker rm -vf $(docker ps -aq)
	docker rmi -f $(docker images -aq)