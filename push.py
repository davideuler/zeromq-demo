import sys
import time

import zmq

context = zmq.Context()
sock = context.socket(zmq.PUSH)
sock.connect(sys.argv[1])
### if we bind on the push server , then send() will block until pull client ready
## if bind on the puller, then send() will not block.

while True:
    print('sending msg')
    sock.send(sys.argv[1] + ':' + time.ctime())  