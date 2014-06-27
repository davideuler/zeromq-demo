<?php

$ctx = new ZMQContext();
$server =
 new ZMQSocket($ctx, ZMQ::SOCKET_REP);
$server->bind("tcp://*:5454");
while(true) {
 $message = $server->recv();
 $server->send($message . " World");
}

?>