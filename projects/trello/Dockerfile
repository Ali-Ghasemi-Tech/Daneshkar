# operatin system and python version
FROM python:3.12-slim

# set working directory
WORKDIR /app

# update packages (optional, can be removed if already updated)
# RUN apt-get update && apt-get install -y libpq-dev

# upgrade pip
RUN pip install --upgrade pip

# copy requirements (assuming your file is named requirements.txt)
COPY ./requirements.txt ./requirements.txt

# install packages (use psycopg2-binary instead)
RUN pip install -r requirements.txt psycopg2

# copy required files
COPY . .

# set env variables
ENV PYTHONUNBUFFERED=1

# run command
CMD [ "python" , 'manage.py' , 'runserver' , '127.0.0.1:8000' ]