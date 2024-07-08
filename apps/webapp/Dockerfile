FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install dumb-init
RUN apt-get update && apt-get install -y dumb-init

# Copy .tar.gz and .whl files to the working directory
COPY /dist/apps/webapp/* /app

# Install built dependencies
RUN pip install --no-cache-dir /app/*.tar.gz

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/app
ENV WEBAPP_HOST=0.0.0.0
ENV WEBAPP_PORT=80
ENV DEBUG_MODE=True
ENV PROD_MODE=True

# Run the webapp
CMD ["dumb-init", "python", "-m", "webapp"]
