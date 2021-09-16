# grpc_test

python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

./grpcurl -plaintext -import-path ~/repos/grpc_test/ -proto ~/repos/grpc_test/calculator.proto -d '{"value":2'} 127.0.0.1:50051 Calculator.SquareRoot