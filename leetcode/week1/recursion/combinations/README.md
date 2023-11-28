# 77. Combinations
Difficult: Medium
Link: https://leetcode.com/problems/combinations/


## Techniques
I didn't complete at the first time, have some sense but the thought was vague.
So after watched solution on YouTube and spent a whole night watch a video teach 3 key techniques to handle backtracking problems
* Choice (at a given state, we could have many decisions or decision space to choose)
* Constraints (at each decision, we could validate if it a good decision, else we could backtrack to the previous decision and go to another decision)
* Goal (which is a final state/ base case we could terminal, which could gain some output or not)


For this problem: 
* At a given state, we could have **n choices** to dive into, when we choose to dive to a choice, our combination will added this choice.
* So if the length of combination = k, we add one combination to the tracking combinations variable so far, then backtrack to the previous decision to choose other decisions.