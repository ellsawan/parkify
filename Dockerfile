# Use an official Node.js runtime as the base image
FROM node:18

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json from the src folder
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all files from the src folder into the container
COPY . .

# Expose the port your application runs on
EXPOSE 3000

# Start the application using App.js
CMD ["node", "App.js"]
