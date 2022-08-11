from collections import deque
from threading import Thread, Lock
import time
from typing import List
from queue import Queue


def ConsumerProducerManual():
    """ using Queue """
    def download(item):
        print("download item ", item)
        return item * 10

    def resize(item):
        print("resize item ", item)
        return item * 100

    def upload(item):
        print("upload item ", item)
        return item * 1000

    class MyQueue:
        def __init__(self) -> None:
            self.items = deque()
            self.lock = Lock()

        def put(self, item):
            with self.lock:
                self.items.append(item)

        def get(self):
            with self.lock:
                return self.items.popleft()

    class worker(Thread):
        def __init__(self, func, in_queue: MyQueue, out_queue: MyQueue, name: str) -> None:
            super().__init__(name=name)
            self.func = func
            self.in_queue = in_queue
            self.out_queue = out_queue
            self.work_done, self.poll_count = 0, 0

        def run(self):
            while True:
                self.poll_count += 1
                try:
                    item = self.in_queue.get()
                except IndexError:
                    time.sleep(0.1)
                else:
                    result = self.func(item)
                    self.out_queue.put(result)
                    self.work_done += 1

    downloadQueue = MyQueue()
    resizeQueue = MyQueue()
    uploadQueue = MyQueue()
    doneQueue = MyQueue()

    threads: List[worker] = [
        worker(download, downloadQueue, resizeQueue, "download"),
        worker(resize, resizeQueue, uploadQueue, "resize"),
        worker(upload, uploadQueue, doneQueue, "upload"), ]

    for t in threads:
        t.start()

    for i in range(10):
        downloadQueue.put(i + 1)
        time.sleep(i * 2)


""" using Queue as a method as it has sleep method """
my_queue = Queue()


class data():
    def __init__(self) -> None:
        self.data = 123


def consumer():
    print("consumer")
    time.sleep(2)
    d = my_queue.get()
    print("queue is done the data was ", d.data)
    my_queue.task_done()
    time.sleep(2)
    d = my_queue.get()
    my_queue.task_done()


thread = Thread(target=consumer)
thread.start()
print("producer")
d = data()
my_queue.put(d)

print("before join")
my_queue.join()
print("doneeee")
my_queue.put(d)

my_queue.join()
print("another done")
