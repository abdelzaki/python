from collections import deque
import heapq
import queue


class Solution:
    def leastInterval(tasks: list[str], n: int) -> int:
        count, idleQueue, maxHeap = dict(), deque(), list()
        time = int()
        for task in tasks:
            count[task] = count.get(task, 0) + 1
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        while maxHeap or idleQueue:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task != 0:
                    idleQueue.append((time + n, task ))
            if idleQueue and idleQueue[0][0] == time:
                heapq.heappush(maxHeap, idleQueue.popleft()[1])
        return time


tasks = ["A", "A", "A", "B", "B", "B"]
n = 2
print(Solution.leastInterval(tasks, n))
