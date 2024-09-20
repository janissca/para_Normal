FROM python:3.12-alpine
WORKDIR /src
COPY kronaclub/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "kronaclub/manage.py", "runserver", "0.0.0.0:8000"]