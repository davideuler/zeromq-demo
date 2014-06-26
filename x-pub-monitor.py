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

def listener_thread (pipe):

    # Print everything that arrives on pipe
    while True:
        try:
            pipe.recv_multipart()
        except zmq.ZMQError as e:
            if e.errno == zmq.ETERM:
                break           # Interrupted

# The main task starts the subscriber and publisher, and then sets
# itself up as a listening proxy. The listener runs as a child thread:

def main ():

    # Start child threads
    ctx = zmq.Context.instance()

    pipe = zpipe(ctx)

    subscriber = ctx.socket(zmq.XSUB)
    subscriber.bind("tcp://*:6000")

    publisher = ctx.socket(zmq.XPUB)
    publisher.bind("tcp://*:6001")

    l_thread = Thread(target=listener_thread, args=(pipe[1],))
    l_thread.start()

    try:
        monitored_queue(subscriber, publisher, pipe[0], 'pub', 'sub')
    except KeyboardInterrupt:
        print ("Interrupted")

    del subscriber, publisher, pipe
    ctx.term()

if __name__ == '__main__':
    main()