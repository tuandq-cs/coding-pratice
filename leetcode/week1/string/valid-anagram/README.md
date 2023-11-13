# 242. Valid Anagram
Difficulty: Easy
Link: https://leetcode.com/problems/valid-anagram/

## Initial thought
* Anagram is a word or phrase formed by rearranging letters of a difference word or phrase
* Using hash table or map to count characters in two 2 string, then compare whether 2 hash table / map is the same

## BigO:
Time Complexity: O(n)
Space Complexity: O(1) because hash table / map with fixed 26 letters in the constraint of input

## Corner cases
* s with one character
