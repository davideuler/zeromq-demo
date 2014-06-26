import zmq
import time
context = zmq.Context()

# create a PUB socket
pub = context.socket (zmq.PUB)
pub.bind("tcp://127.0.0.1:5566")
# push some message before connected
# these messages are dropped
for i in range(5):
    pub.send('test a message should not be dropped')

time.sleep(1)

# create a SUB socket
sub = context.socket (zmq.SUB)
sub.connect("tcp://127.0.0.1:5566")
sub.setsockopt(zmq.SUBSCRIBE, "te")

time.sleep(1)

# this is the message we should see in SUB
pub.send('test hi')
pub.send('test hello')

while True:
    print repr(sub.recv())