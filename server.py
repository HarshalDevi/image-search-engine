import grpc
from concurrent import futures
import image_search_pb2
import image_search_pb2_grpc
import os
import random

class ImageSearchServicer(image_search_pb2_grpc.ImageSearchServicer):
    def SearchImage(self, request, context):
        image_dir = '/app/dataset/' + request.keyword
        image_files = os.listdir(image_dir)
        print(image_files)
        image_file = random.choice(image_files)
        with open(os.path.join(image_dir, image_file), 'rb') as f:
            image_data = f.read()
        return image_search_pb2.ImageResponse(image_data=image_data)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    image_search_pb2_grpc.add_ImageSearchServicer_to_server(ImageSearchServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
