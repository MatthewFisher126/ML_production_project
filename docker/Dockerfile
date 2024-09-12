# Use an official Python runtime as a parent image
FROM python:3.9.16

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME=MLops_env

# Run python when the container launches
CMD ["python3"]
