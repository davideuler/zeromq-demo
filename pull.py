## usage pull.py tcp://localhost:3100
import zmq
import sys

ctx = zmq.Context()
s = ctx.socket(zmq.PULL)
s.connect(sys.argv[1])
while True:
    msg = s.recv()
    print 'Got msg:', msg 