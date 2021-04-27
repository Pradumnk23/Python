import threading
from time import sleep

class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            sleep(1)

x = Messenger(name='Send out messages')
y = Messenger(name='Recieve messages')
x.start()
sleep(0.2)
y.start()
# Here x and y runs simultaneously , they dont wit for finish x nd then for running y...
# This system is used in maybe all the messenger application , like whatsup, mesu..
# look carefull the process of sleep..