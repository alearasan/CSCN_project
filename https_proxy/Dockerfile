# Use a base image with Nginx pre-installed
FROM nginx:latest

# Remove default nginx configuration
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom nginx configuration
COPY nginx_config/nginx.conf /etc/nginx/nginx.conf

# Create a directory to store SSL certificates
RUN mkdir -p /etc/nginx/certs

# Copy SSL certificates to the container
COPY certificates/ssl_certificate.crt /etc/nginx/certs/
COPY certificates/ssl_certificate_key.key /etc/nginx/certs/

# Expose HTTPS port
EXPOSE 443

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
