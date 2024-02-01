FROM --platform=linux/amd64 python:3.10.9-slim-buster
LABEL maintainer="chemuranov@gmail.com"

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .

RUN python manage.py migrate
RUN python manage.py loaddata fixture.json

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]