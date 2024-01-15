FROM python:3.10-slim

# Author information
LABEL maintainer="demousr@gmail.com"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./SampleApp/ /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set env variable
ENV user admin
ENV password password
# Or in single line: ENV user=admin password=password

# Expose port 8080 for the application
EXPOSE 5000

CMD ["python", "test.py"]
