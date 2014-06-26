# Espresso Pattern
# This shows how to capture data using a pub-sub proxy
#

import time

from random import randint
from string import uppercase
from threading import Thread

import zmq
from zmq.devices import monitored_queue

from zhelpers import zpipe

# The subscriber thread requests messages starting with
# A and B, then reads and counts incoming messages.

def subscriber_thread():
    ctx = zmq.Context.instance()

    # Subscribe to "A" and "B"
    subscriber = ctx.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:6001")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"A")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"B")

    count = 0
    while True:
        try:
            msg = subscriber.recv_multipart()
            print('msg got by client:%s' % msg)
        except zmq.ZMQError as e:
            if e.errno == zmq.ETERM:
                break           # Interrupted
            else:
                raise
        count += 1

    print ("Subscriber received %d messages" % count)

# The publisher sends random messages starting with A-J:

def publisher_thread():
    ctx = zmq.Context.instance()

    publisher = ctx.socket(zmq.PUB)
    publisher.connect("tcp://localhost:6000")

    while True:
        string = "%s-%05d from publisher" % (uppercase[randint(0,10)], randint(0,100000))
        try:
            publisher.send(string)
        except zmq.ZMQError as e:
            if e.errno == zmq.ETERM:
                break           # Interrupted
            else:
                raise
        time.sleep(0.1)         # Wait for 1/10th second


# The main task starts the subscriber and publisher, and then sets
# itself up as a listening proxy. The listener runs as a child thread:

def main ():

    # Start child threads
    p_thread = Thread(target=publisher_thread)
    s_thread = Thread(target=subscriber_thread)
    p_thread.start()
    s_thread.start()

if __name__ == '__main__':
    main()