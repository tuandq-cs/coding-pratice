class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        z = [0 for i in range(n)]
        l = 0
        r = -1
        for i in range(1, n):
            # init start at
            if i > r:
                z[i] = 0
            else:
                z[i] = min(z[i-l], r-i+1)
            # adjust z[i]
            while (i + z[i] < n and s[i+z[i]] == s[z[i]]):
                z[i] += 1
            # update [l, r] by [cur, cur+z[i]-1]
            if (r < i + z[i]):
                l = i
                r = i + z[i] - 1
            if i + z[i] == n:
                return s[:z[i]]
        return ""
            