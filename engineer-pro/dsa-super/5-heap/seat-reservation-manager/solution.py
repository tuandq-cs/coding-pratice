import heapq

class SeatManager:

    def __init__(self, n: int):
        self.pq = []
        for i in range(1, n+1):
            heapq.heappush(self.pq, i)

    def reserve(self) -> int:
        t = heapq.heappop(self.pq)
        return t


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.pq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)