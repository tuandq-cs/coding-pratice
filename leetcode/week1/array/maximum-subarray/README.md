### 53. Maximum Subarray
Difficulty: Medium
Link: https://leetcode.com/problems/maximum-subarray/

## Initial thought
My very first thought is kinda vague, the idea is nearly the same after I read solution, which don't know how to explain clearly
But there're some points I can speak out when I'm in an interview
* Subarray: is a subset of collection of items in the parent array, so that the order will be remain without missing any item
* Subarray will have at least 1 item -> can define the start,end index & these index can overlap each other (start=end)
* nums[i] can be negative, because a subarray of only positive nums always increase when the length of subarray get larger

## Techniques
* Precompute prefix sum
## Solution
I found a solution on Youtube which is Kadane's algorithm
Here is the idea:
* At any item: assume we already precomputed our concerned subarray from the previous step (here has maximum sum), called M and the item itself x
* At this time, we can determine the concerned subarray at the next item (iteration) by compare subarray [M x] and x. If sum of [M x] < x, the subarray for next item will be [x], else the subarray has x as a new item, so the subarray for next time will be [M x]
* **Initial step** is very important right there, at the first iteration, the current subarray is empty so the subarray for next iteration will be [x]
* Use a global variable for track which subarray has the maximum sum

## BigO
* Time complexity: O(n) because for each iteration, we already has the current maximum sum subarray which is computed from previous step
* Space complexity: O(1), because we just use 2 variable for tracking the current maximum subarray & the global one

## Corner cases
* Just one has item