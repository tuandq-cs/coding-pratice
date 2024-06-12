class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)
        # ring = "dcaxace"
        #               ^
        # key = "adcde"
        #            ^
        pos = {}
        for i in range(n):
            c = ring[i]
            if pos.get(c) is None:
                pos[c] = []
            pos[c].append(i)
        memo = {}
        def recur(iRing, iKey):
            if iKey == m:
                return 0
            if (iKey, iRing) in memo:
                return memo[(iKey, iRing)]
            # have pos[key[iKey]] choices to reach key[iKey]
            minSteps = float('inf')
            for i in pos[key[iKey]]:
                # calc steps
                steps = abs(i - iRing)
                steps = min(steps, n-steps)
                minSteps = min(minSteps, steps + recur(i, iKey+1))
            memo[(iKey, iRing)] = minSteps + 1
            return minSteps + 1
        return recur(0, 0)

