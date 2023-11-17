# 3. Longest Substring Without Repeating Characters

Difficulty: Medium
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/


## Initial thought
* Substring: contiguous non-empty of chars
* Longest substring **without repeating elements**
* s can be empty => longest length = 0
* s letters, digits, symbols, spaces

## Solution
* Use 2 pointers, left pointer is used to track the first element of **current longest substring without repeating chars**, right pointer to iterate through whole string as the end element of the concerned substring
* Use hash table / map to track the latest index of the char
* At any right pointer, if the char at this pointer is **existed in the hash table / map** & **the latest index of the char >= the left pointer**
* Update the left pointer = the latest index of the char + 1
* Track the global longest length at any right pointer iteration
## BigO
Time Complexity: O(n)
Space Complexity: O(1) because map has fixed 26 keys
## Corner cases
* s is empty, s = ""
* s with repeated items, s = "bbb"
