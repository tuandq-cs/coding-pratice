# 49. Group Anagrams
Difficulty: Medium
Link: https://leetcode.com/problems/group-anagrams/

## Initial thought 

## Techniques:
* Use hash table to group anagrams, these anagrams in the same group will have the same key in hash table
* Hash function will be very important in this problem
* Make sure the hash function doesn't lead to collisions, which is has the same key
* At my first solution, I create a bad hash function that given a string, transform each letter to integer in ASCII table, then assign the counter in the array of 26 items, which is ordered from a-z. Then I join all ordered-counter of letters to a string as a key in hash function
* Ex: string: abca -> counter array: [2, 1, 1] -> key: "211"
* But the transformation step is the main pain point, because integer is very dangerous when join together, Ex: [2, 1, 1] has key "211", but [21, 1] also has key "211" -> which lead to collisions :'(
* So just 