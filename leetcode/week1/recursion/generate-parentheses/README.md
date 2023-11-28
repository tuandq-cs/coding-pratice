# 22. Generate Parentheses
Difficulty: Medium
Link: https://leetcode.com/problems/generate-parentheses

## Techniques:
At first, I was struggle to solve this problem. After learn how to solve **backtrack** problem with 3 keys, I solved this problem okay.

So:
* At each state, we could 2 decisions ( or ) to choose
* If used open parenthesis so far < n, we could have a possible decision is to add an open parenthesis
* If used open parenthesis so far < used close parenthesis, we could have a possible decision is to add a closed parenthesis
* If used close parenthesis = n (the base case), we add the combination so far to result. 