class Allocator:

    def __init__(self, n: int):
        self.memo = [-1 for _ in range(n)]

    def allocate(self, size: int, mID: int) -> int:
        i, j = 0, 0
        while (i < len(self.memo)):
            while (j < len(self.memo) and self.memo[i] == self.memo[j]):
                if self.memo[i] == -1 and j - i + 1 == size:
                    for k in range(i, j+1):
                        self.memo[k] = mID
                    return i
                j += 1
            i = j
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for i in range(len(self.memo)):
            if self.memo[i] == mID:
                self.memo[i] = -1
                cnt +=1
        return cnt
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)