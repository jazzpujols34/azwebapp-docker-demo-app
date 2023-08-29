# Use an official Python runtime as a base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --trusted-host pypi.python.org Flask

# Make port 5000 available to the world outside this container
EXPOSE 5011

# Run app.py when the container launches
CMD ["python", "app.py"]



