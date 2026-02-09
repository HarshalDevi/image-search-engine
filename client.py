import grpc
import image_search_pb2
import image_search_pb2_grpc
import os

def run():
    keyword = input("Enter keyword: ")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = image_search_pb2_grpc.ImageSearchStub(channel)
        try:
            response = stub.SearchImage(image_search_pb2.SearchRequest(keyword=keyword))
            if response.image_data:
                filename = f'{keyword}'+'.jpg'
                with open(filename, 'wb') as f:
                    f.write(response.image_data)
                print(f"Image received successfully for keyword '{keyword}'.")
                open_image(filename)
            else:
                print(f"No image found for the keyword '{keyword}'.")
        except grpc.RpcError as rpc_error:
            if rpc_error.code() == grpc.StatusCode.UNKNOWN:
                print(f"No image found for the keyword '{keyword}'.")
            else:
                print(f"Unexpected gRPC error: {rpc_error}")
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
def open_image(filename):
    try:
        # Open the image file using the default image viewer
        os.startfile(filename)
    except Exception as e:
        print(f"Error opening image file: {e}")

if __name__ == '__main__':
    run()
