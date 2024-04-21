import heapq


class MedianFinder:

    def __init__(self):
        self.lower = [] # maxHeap
        self.higher = [] # minHeap

    def addNum(self, num: int) -> None:
        # I want len(lower) >= len(higher)
        if len(self.lower) == len(self.higher):
            heapq.heappush(self.higher, num) # minH
            v = heapq.heappop(self.higher)
            heapq.heappush(self.lower, v*-1) # maxH
        else:
            # self.lower > self.higher, actually self.lower + 1 == self.higher
            heapq.heappush(self.lower, num*-1) # maxH
            v = heapq.heappop(self.lower)
            heapq.heappush(self.higher, v*-1)

    def findMedian(self) -> float:
        # Constraint: There will be at least one element in the data structure before calling findMedian.
        #print(self.lower, self.higher)
        if len(self.lower) == len(self.higher):
            return (self.lower[0]*-1 + self.higher[0]) / 2
        return self.lower[0]*-1

    # l = [1]
    # h = [2]
    # med = 1.5
    # 3
    # med = [-1, -1.5]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()