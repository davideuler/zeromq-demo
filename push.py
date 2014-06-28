import sys
import time

import zmq

context = zmq.Context()
sock = context.socket(zmq.PUSH)
sock.bind(sys.argv[1])

while True:
    print('sending msg')
    sock.send(sys.argv[1] + ':' + time.ctime())