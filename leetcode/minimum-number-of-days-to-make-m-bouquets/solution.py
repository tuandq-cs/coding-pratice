from typing import List


class Solution:
    def countBouquets(self, bloomDay: List[int], m: int, k: int, days: int) -> int:
        cnt = 0
        bloomFlowers = 0
        for d in bloomDay:
            if bloomFlowers == k:
                cnt += 1
                bloomFlowers = 0
            if days >= d:
                bloomFlowers += 1
            else:
                bloomFlowers = 0
        return cnt + 1 if bloomFlowers == k else cnt

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        res = -1
        while (l <= r):
            days = l + (r-l)//2
            cnt = self.countBouquets(bloomDay, m, k, days)
            if cnt >= m:
                res = days
                r = days - 1
            else:
                l = days + 1
        return res
