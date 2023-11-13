# 125. Valid Palindrome
Difficulty: Easy
Link: https://leetcode.com/problems/valid-palindrome/

## Initial thought
* As the description, a phrase need to process to a string, then check if this string is palindrome
* Step 1: Pre-process the phrase to a string
* Step 2: Use 2 pointers from the left & right, if any values of 2 pointers doesn't match return False, else True

## Optimal solution
After reading solution,first step could result in Space Complexity: O(n), I can do it this step in step 2 by ignoring redundant characters, then move the pointer as their direction

## BigO
Time Complexity: O(n)
Space Complexity: O(1)