# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory in Docker
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install tkinter dependencies
RUN apt-get update && apt-get install -y tk

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Notepad

# Run notepad.py when the container launches
CMD ["python", "notepad.py"]
