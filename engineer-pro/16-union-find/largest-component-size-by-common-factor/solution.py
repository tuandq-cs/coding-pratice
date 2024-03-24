from typing import List


class Solution:
    def findPrime(self, maxNum: int) -> List[int]:
        p = 2
        prime = [1 for _ in range(maxNum+1)]
        prime[0] = 0
        prime[1] = 0
        while (p*p <= maxNum):
            if prime[p]:
                # update prime = 0 for all multiple of p
                for i in range(p*p, maxNum+1, p):
                    prime[i] = 0
            p += 1
        res = []
        for p in range(2, maxNum + 1):
            if prime[p]:
                res.append(p)
            p+=1
        return res

    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x: int):
            if parent[x] == x: return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(u: int, v: int):
            x = find(u)
            y = find(v)
            if x == y:
                return
            if rank[x] > rank[y]:
                parent[y] = x
            else:
                parent[x] = y
                if rank[x] == rank[y]:
                    rank[y] += 1

        n = len(nums)
        maxNum = max(nums)
        parent = [-1] * (maxNum+1)
        rank = [-1] * (maxNum+1)
        for i in nums:
            parent[i] = i
            rank[i] = 0
        primeNums = self.findPrime(maxNum) # Time: O(m*log(log(m)))
        for i in primeNums:
            parent[i] = i
            rank[i] = 0
        for p in primeNums:  # Time: O(m*log(log(m)))
            for num in range(p*2, maxNum+1, p):
                if parent[num] != -1:
                    union(num, p)
        mParent = {}
        for i in nums:
            p = find(i)
            mParent[p] = mParent.get(p, 0) + 1
        res = 0
        for p in mParent:
            res = max(mParent[p], res)
        return res
        # # Time: O(m*log(log(m))), m is max in nums
        # 1 <= n <= 2*10^4
        # 1 <= m <= 10^5
    
nums = [4,6,15,35]
#         ^

# primes = [2, 3, 5]
#              ^

# 2 -> 4 -> 6
# 3 -> 15
# 5 -> 35


nums = [20,50,9,63]

# primes = [2,3,5,7]

# 2 -> 20 -> 50
# 3 -> 9 -> 63

nums = [2,3,6,7,4,12,21,39]

# primes = [2, 3, 5]

# out = Solution().largestComponentSize(nums)
# print(out)
    

