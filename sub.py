import zmq 
import time
context = zmq.Context()
forward_socket = context.socket(zmq.SUB)
forward_socket.connect("tcp://127.0.0.1:7002")
forward_socket.setsockopt(zmq.SUBSCRIBE, 'orderbook')
time.sleep(1)
while True:
  print 'receiving' 
  transpport = forward_socket.recv()
  print transpport
  print 'parsing data' 
  transpport = transpport.split('orderbook ')[1]
  print 'msg:%s' % transpport