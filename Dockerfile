# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy necessary files
COPY farmers-protest-tweets-2021-2-4.json /app/farmers-protest-tweets-2021-2-4.json
COPY challenge.ipynb /app/challenge.ipynb
COPY requirements.txt /app/requirements.txt
COPY src /app/src
COPY uwsgi.ini /app/uwsgi.ini
COPY entrypoint.sh /app/entrypoint.sh
COPY main.py /app/main.py

# Install build-essential and other dependencies, including OpenJDK
RUN apt-get update && apt-get install -y build-essential openjdk-11-jdk

# Verify Java installation
RUN ls -la /usr/lib/jvm && ls -la /usr/lib/jvm/java-11-openjdk-arm64/bin/java

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jupyter uwsgi

# Make ports 80 and 8888 available to the world outside this container
EXPOSE 80
EXPOSE 8888

# Define environment variables for Jupyter Notebook and Spark
ENV JUPYTER_NOTEBOOK_DIR /app
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-arm64
ENV PATH $JAVA_HOME/bin:$PATH
ENV PYSPARK_PYTHON python3

# Set the entrypoint to the script
ENTRYPOINT ["/app/entrypoint.sh"]
