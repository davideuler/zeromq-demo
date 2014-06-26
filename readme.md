
pub.py, sub.py : it shows how to subscribe messages from a zmq socket server 两个文件结合使用
x-pub.py: it shows how to use xsub & xpub in a single file  一个文件，完整的xpub,xsub示例

no-bubfer.py: a demo for sub and pub. 一个文件中，同时有sub和pub

an example for multi process, multi publisher, multi subscriber, 多个进程，多个publisher, 多个subscriber的例子
x-pub-client-2.py
x-pub-client.py
x-pub-monitor.py

Firstly, you start the x-pub-monitor.py,
then you can start x-pub-client.py, and x-pub-client2.py, and you will see that the two process will subscribed the same messages.
For easier comparison, I suggest to view the message recieving process in two vertical panel in tmux (http://tmux.sourceforge.net/):
In tmux, press Ctrl+B,% to split the screen vertically. Then Ctrl+B+Left, Ctrl+B+Right to swith the two panel.
You can start x-pub-client.py in the left panel of tmux, and x-pub-client-2.py in the right panel.
 
