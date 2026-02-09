# Project Assignment 2: gRPC-Backed Image Search Engine

## Create necessary files
* To implement the multi-threaded server for the image search engine using gRPC and containerize it using Docker, we need to create necessary files first.
* Created Protobuf File (.proto):

Created a file named ```image_search.proto``` to define the service methods and message types:

The below command generates Go code for Protocol Buffers and gRPC from the image_search.proto file, with output paths relative to the source directory.
```
protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative image_search.proto
```
The below command compiles the image_search.proto file into Python code for Protocol Buffers and gRPC, with output in the current directory.
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. image_search.proto
```

This will generate ```image_search.pb.go``` and ```image_search_grpc.pb.go``` for Go, and you'll need to install the ```grpcio-tools``` package for Python.


 
## Implement Server (Python): (server.py)

## Implement Client (Python): (client.py)

## Implement Client (GO) : (client.go)


## Dockerize the Server
Created a Dockerfile (Dockerfile) to containerize the server:

Created  a ````requirements.txt```` file if you have any dependencies.

## Build the Docker image:
```
docker build -t image_search_server .
```
## Run the Docker container with the dataset volume mounted:
```
docker run -d --name image_search_server -v C:\dataset:/app/dataset -p 50051:50051 image_search_server

```
## Run Python Client:
```
python client.py
```
## Run Go Client:
```
go run client.go
```
# Unusual Fact : 
Every time you run client code you will see random images of that particular keyword in this case you will see two random images for a particular keyword.

# References :
* https://grpc.io/docs/what-is-grpc/introduction/ 
* https://docs.docker.com/get-started/overview/
* https://docs.docker.com/get-started/
* https://grpc.io/docs/languages/
