import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.cnt = 1
        self.pq = []
        self.s = set()

    def popSmallest(self) -> int:
        if len(self.pq) == 0:
            self.cnt += 1
            return self.cnt - 1
        num = heapq.heappop(self.pq)
        self.s.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num >= self.cnt or num in self.s:
            return
        heapq.heappush(self.pq, num)
        self.s.add(num)

    # k: total numbers was added back to heap
    # addBack: O(k*log(k))
    # popSmallest: O(k*log(k))
    # overall: O(k*log(k)) in time and space



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)