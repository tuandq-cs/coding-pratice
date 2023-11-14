from typing import List


def getKey(s: str):
    counter = [0] * 26
    for c in s:
        i = ord(c) - ord('a')
        counter[i] += 1
    k = ""
    for i, c in enumerate(counter):
        if c == 0:
            continue
        k += f"{c}{chr(ord('a') + i)}"
    return k


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_map: dict[str, str] = {}
        for s in strs:
            k = getKey(s)
            if group_map.get(k) is None:
                group_map[k] = []
            group_map[k].append(s)
        return [group_map[k] for k in group_map]
        # Time: O(n.max(m)), n: length of strs, m: length of strs[i]
        # Space: O(n), in worst case: each key assign each strs[i]


# General cases
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]
# group_map = {
#   "1a1e1t": ["eat", "tea", "ate"]
#   "1a1n1t": ["tan", "nat"]
#   "1a1b1t": ["bat"]
# }
result = Solution().groupAnagrams(strs)
print(result)

# Corner cases
# strs has 1 item with empty string
# Expected = [[""]]
strs = [""]
# group_map = {
#   "": [""]
# }
result = Solution().groupAnagrams(strs)
print(result)

# strs has duplicate items
strs = ["", "", ""]
# Expected = [["", "", ""]]
result = Solution().groupAnagrams(strs)
print(result)

strs = ["bdddddddddd", "bbbbbbbbbbc"]
# group_map = {
#   "1b10d": ["bdddddddddd"]
#   "10b1c": ["bbbbbbbbbbc"]
# }
result = Solution().groupAnagrams(strs)
print(result)
