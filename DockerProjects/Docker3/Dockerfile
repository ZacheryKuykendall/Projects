# Use the official Node.js image as the base image
FROM node:14

# Set the working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the application dependencies
RUN npm install

# Copy the application code to the working directory
COPY . .

# Expose the application port
EXPOSE 3001

# Start the application
CMD [ "node", "app.js" ]
