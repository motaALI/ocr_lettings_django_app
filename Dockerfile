# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project code into the container
COPY . .

# Expose the port number that Django runs on
EXPOSE $PORT

# Define the command to run the application
CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT
