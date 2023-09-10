# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory content into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Specify the command to run on container start
CMD ["python", "app.py"]
