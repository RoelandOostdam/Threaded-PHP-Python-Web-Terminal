from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg):
        print "running"
        sleep(1)


if __name__ == "__main__":
    thread = Thread(target = threaded_function, args = (10, ))
    thread2 = Thread(target = threaded_function, args = (10, ))
    thread.start()
    thread2.start()
    thread.join()
    thread2.join()
    print "thread finished...exiting"