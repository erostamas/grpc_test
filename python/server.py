#!/usr/bin/env python3
import grpc

import calculator_pb2
import calculator_pb2_grpc
import calculator

import concurrent.futures
import time

class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = calculator.square_root(request.value)
        return response


server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))

calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)

print("Starting server, listennig on port 50051")
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)