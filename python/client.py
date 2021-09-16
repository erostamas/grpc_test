#!/usr/bin/env python3

import grpc
import calculator_pb2
import calculator_pb2_grpc
import sys

try:
    channel = grpc.insecure_channel('localhost:50052')

    stub = calculator_pb2_grpc.CalculatorStub(channel)

    number = calculator_pb2.Number(value = float(sys.argv[1]))
    response = stub.SquareRoot(number)
    print(response.value)

except Exception as e:
    print(e)