# 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## Initial thought
* The sell day must be later than the buy day
* To capture profit: The price at sell day must be > than the price at buy day
=> Find sub period that increasing until the end of period
=> From all sub periods, find the global max between periods
## Techniques
**Slicing window**: use 2 pointers that move in the same direction and will **never overtake each other** (the thing can happen on two pointers technique)

* Step 1: Assign the left and right pointer at the same position
* Step 2: Move the right pointer to the end
  * If price[right] > price[right], capture profit, determine global maximum profit
  * Else: Do Step 1

## BigO:
Time Complexity: O(n)
Space Complexity: O(1), 2 pointer index, global maximum profit

## Corner cases
* Always drop period -> The left point will be assigned to the right point
* Always rise/unchanged period -> The right point will move til the end without assignment