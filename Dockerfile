# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the project code into the container
COPY . /app/

# Run the application using Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi", "--bind", "0.0.0.0:8000"]
