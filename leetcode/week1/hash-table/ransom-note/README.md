# 383. Ransom Note
Difficulty: Easy
Link: https://leetcode.com/problems/ransom-note/

##Simple solution:
  
* Use 2 hash map to count has many letters for each letter, letter is the key of hash map
* Compare 2 hash map, if the first hash map didn't have the key of the second hash map return False
* Or even if they has the same key but has different counter, return False