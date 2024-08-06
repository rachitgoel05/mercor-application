# frontend/Dockerfile
FROM node:16

# Set the working directory in the container
WORKDIR /frontend/employee-information

# Copy the package.json and package-lock.json (if available)
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code into the container
COPY . .

# Build the React app
RUN npm run build

# Use the official Nginx image to serve the React app
FROM nginx:alpine
COPY --from=0 /frontend/employee-information/build /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
