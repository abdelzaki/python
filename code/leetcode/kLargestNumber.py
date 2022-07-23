import heapq
"""Design a class to find the kth largest element in a stream.
 Note that it is the kth largest element in the sorted order, 
 not the kth distinct element."""
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.minHeap = nums
        self.index = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap,val)
        while len(self.minHeap) > self.index:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


klargest = KthLargest(3,[4,5,8,2])
print(klargest.add(3))     
print(klargest.add(5))     
print(klargest.add(10))     
print(klargest.add(9))  
print(klargest.add(4))     


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)