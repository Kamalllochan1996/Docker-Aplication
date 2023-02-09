# Use an official Python runtime as the base image
FROM python:3.10-slim-buster

# Copy the local application files to the container
COPY C:\Users\kAMAL\DOCKER_WEATHER\myapp /app

# Copy the local requirements.txt file to the container
COPY requirements.txt ./

# Install the required packages
RUN pip install -r requirements.txt

# Copy the local application files to the container
COPY . .

# Expose the port that the application will listen on
EXPOSE 8000


ENV DJANGO_SETTINGS_MODULE=myapp.settings

# Set the default command to run when starting the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]