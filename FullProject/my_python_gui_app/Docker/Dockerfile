FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install tkinter dependencies
RUN apt-get update && apt-get install -y tk

# Copy the current directory contents into the container at /app
COPY . /app

# Set the command to run your app
CMD ["python", "./app.py"]
