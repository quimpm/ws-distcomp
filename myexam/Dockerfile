FROM python:3.9-buster

# Set environment variables.
# PYTHONDONTWRITEBYTECODE prevents Python from writing pyc files to disc.
# PYTHONUNBUFFERED Prevents Python from buffering stdout and stderr.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app so any further instructions on the dockerfile
# occur within this directory.
RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get -y install libpng-dev zlib1g-dev curl unzip
#RUN apt-get install linux-headers
# Copy the requirements file into the image's filesystem at /app directory.  postgresql-12
RUN apt-get -y install gcc python3-dev musl-dev

COPY requirements.txt /app/

# Install dependencies.
RUN pip install -r requirements.txt

# Copy the current directory contents into the image's filesystem at /app directory.
COPY . /app

# Create and switch to a user who will run our application instead of the root
# user (security measure applied in case the application is hacked).
RUN adduser runner
USER runner