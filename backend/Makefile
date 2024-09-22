

build:
	docker build -t my_django_app .
	docker run -d --name backend -p 8000:8000 my_django_app

run:
	docker run -d --name backend -p 8000:8000 my_django_app
# docker run --name some-redis -p 6379:6379 -d redis
# 
stop:
	docker stop backend

clean:
	docker stop backend
	docker remove backend
	docker rmi my_django_app
