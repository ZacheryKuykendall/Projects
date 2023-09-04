# Use an official Node runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install application dependencies
RUN npm install

# Set environment variables if needed
# ENV NODE_ENV=production

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the application
CMD ["npm", "start"]
