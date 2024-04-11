class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mS = {}
        mT = {}
        for c in s:
            mS[c] = mS.get(c, 0) + 1
        for c in t:
            mT[c] = mT.get(c, 0) + 1
        overlap = 0
        for c in mS:
            if mT.get(c):
                overlap += min(mS[c], mT[c])
        return len(s) - overlap