"""
to enable multi threads
"""
# the start would start when u call run till then the thread wont start
from concurrent.futures import thread
import time
from threading import Thread


def func(n, p):
    while n > 0:
        print(n)
        n -= 1
        time.sleep(2)


def testThread():
    x = 12
    t = Thread(target=func, args=(5, x))
    t.start()
    print("before join")
    t.join()
    print("after join")

# to program thread which is pollable


class clsPollable():
    def __init__(self) -> None:
        self.terminated = False

    def run(self, n):
        print("n " ,n)
        while n > 0 and not self.terminated:
            print(n)
            n -= 1
            time.sleep(2)

    def terminate(self):
        self.terminated = True


def testPollabe():

    cls = clsPollable()
    t = Thread(target=cls.run, args=(5,))
    t.start()
    print("before join")
    time.sleep(4)
    cls.terminate()
    t.join()
    print("after join")


testPollabe()
