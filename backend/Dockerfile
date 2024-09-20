FROM python:3.12-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN cd kronaclub && python manage.py makemigrations  && python manage.py migrate && python manage.py fill_db
EXPOSE 8000
CMD ["python", "kronaclub/manage.py", "runserver", "0.0.0.0:8000"]
# docker stop backend
# docker remove backend
# docker rmi my_django_app
# docker build -t my_django_app . 
# docker run -d --name backend -p 8000:8000 my_django_app