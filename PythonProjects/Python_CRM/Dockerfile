# Use a base Python image that contains the necessary dependencies for tkinter
FROM python:3.8

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install tkinter using the package manager
RUN apt-get update && apt-get install -y python3-tk

# Make port 80 available to the world outside this container
EXPOSE 80

# Run your application
CMD ["python", "./crm_app.py"]
