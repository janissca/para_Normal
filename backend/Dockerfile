FROM python:3.12-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN cd kronaclub && python manage.py makemigrations && python manage.py makemigrations users eventsapp && python manage.py migrate && python manage.py fill_db
EXPOSE 8000
CMD ["gunicorn", "--workers=3", "--bind", "0.0.0.0:8000", "kronaclub/kronaclub.wsgi:application"]
