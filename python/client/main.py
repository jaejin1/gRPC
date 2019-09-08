"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import random
import logging

import grpc

import hi_pb2
import hi_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hi_pb2_grpc.HiStub(channel)

        ## JaejinHi
        response = stub.JaejinHi(hi_pb2.HiRequest(name='test test test test !!'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()