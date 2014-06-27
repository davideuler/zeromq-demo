<?php                                                                                             │
$ctx = new ZMQContext();                                                                          │
$publisher=                                                                                       │
 new ZMQSocket($ctx, ZMQ::SOCKET_PUB);                                                            │
$publisher->connect("tcp://localhost:6000");                                                      │
sleep(1);                                                                                         │
                                                                                                  │
$publisher->send("postweibo 12294");                                                              │
                                                                                                  │
?>