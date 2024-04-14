from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        q = []
        mIndex = {} # map[char]index in q
        for c in s:
            if mIndex.get(c) is None:
                q.append({c})
                mIndex[c] = len(q) - 1
            else:
                qIndex = mIndex[c]
                newSet = set()
                for _ in range(len(q)-qIndex):
                    tmp = q.pop()
                    for c in tmp:
                        newSet.add(c)
                        mIndex[c] = qIndex
                q.append(newSet)
        ans = []
        cnt = 0
        curIndex = 0
        for c in s:
            if mIndex[c] != curIndex:
                ans.append(cnt)
                cnt = 0
                curIndex = mIndex[c]
            cnt += 1
        ans.append(cnt)
        return ans
        # Time: O(n*24), n is length of s
    
s = "ababcbacadefegdehijhklij"
# q = [a, b]
# 
s = "eccbbbbdec"
out = Solution().partitionLabels(s)
print(out)