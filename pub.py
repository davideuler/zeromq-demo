#coding=utf-8
import zmq
import json,time

ctx = zmq.Context()
forward_socket = ctx.socket(zmq.PUB)
forward_socket.bind("tcp://127.0.0.1:7002")
transpport = 'orderbook stuff'
time.sleep(1)

print('publish data')
forward_socket.send(transpport)