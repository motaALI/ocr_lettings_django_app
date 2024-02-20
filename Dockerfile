# Use a slim Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app


# Upgrade pip and install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*


# Copy only the requirements file into the container at /app
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install gunicorn

# Copy the rest of the application code into the container at /app
COPY . .

# Collect static files during the Docker build
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable for Django
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings

# Update STATIC_ROOT path
ENV STATIC_ROOT=/app/staticfiles/

# Set correct permissions for static files
# RUN chmod -R 755 /app/staticfiles/

# Run the application using Gunicorn
CMD ["gunicorn", "oc_lettings_site.wsgi", "--bind", "0.0.0.0:8000"]
