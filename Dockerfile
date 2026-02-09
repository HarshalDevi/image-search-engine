# Use the official Python image as the base image for server and Python client
FROM python:3.8-slim AS server_python_client

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the server Python script and generated proto files into the container
COPY server.py .
COPY image_search_pb2.py .
COPY image_search_pb2_grpc.py .

# Expose the port on which the gRPC server will listen
EXPOSE 50051

# Command to run the server when the container starts
CMD ["python", "server.py"]

# Use the official Golang image as the base image for Go client
FROM golang:1.17 AS client_go

# Set the working directory in the container
WORKDIR /go/src/app

# Copy the Go client source code into the container
COPY client.go .

# Install the grpc package
RUN go get -u google.golang.org/grpc

# Build the Go client binary
RUN go build -o client client.go
# Command to run the Go client
CMD ["go", "run", "client.go"]

# Use Python image as the base image for Python client
FROM python:3.8-slim AS client_python

# Set the working directory in the container
WORKDIR /app

# Copy the Python client script and generated proto files into the container
COPY client.py .
COPY image_search_pb2.py .
COPY image_search_pb2_grpc.py .

# Install grpcio and protobuf packages
RUN pip install --no-cache-dir grpcio protobuf
# Install catimg
RUN apt-get update && apt-get install -y catimg

# Command to run the Python client
CMD ["python", "client.py"]
