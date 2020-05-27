from concurrent import futures
import grpc
import time

import reversing_pb2
import reversing_pb2_grpc

class TextResponseServicer(reversing_pb2_grpc.TextResponseServicer):
    def ReversingText(self, request, context):
        print('Client Connected and send request: ' + request.data)
        response = reversing_pb2.Text()
        response.data = request.data[::-1]
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    reversing_pb2_grpc.add_TextResponseServicer_to_server(TextResponseServicer(), server)
    print('Starting server! On port 50000')
    server.add_insecure_port('[::]:50000')
    server.start()

    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        server.stop(0)




if __name__ == '__main__':
    serve()