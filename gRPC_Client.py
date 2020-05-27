import grpc

import reversing_pb2
import reversing_pb2_grpc

channel = grpc.insecure_channel('localhost:50000')
stub = reversing_pb2_grpc.TextResponseStub(channel)

text = 'doc teyamol aytsok'

to_response = reversing_pb2.Text(data=text)
response = stub.ReversingText(to_response)
print(response.data + " - Красавчик")