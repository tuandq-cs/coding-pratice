# 238. Product of Array Except Self

Difficulty: Medium
Link: https://leetcode.com/problems/product-of-array-except-self/

## Initial thought
* The product of suffix & prefix will be int64 at minimum
* O(n) + don't use division operation
* answers = product of prefix * product of suffix
* Traversing the array twice, the first one will compute the product of prefix, the second is for product of suffix
* Use 2 arrays to store these products -> Space Complexity: O(n)
* Can optimize by write product of prefix to answers, then write product of suffix

## Techniques
- **Precomputation**: For questions where summation or multiplication of a subarray is involved, pre-computation using hashing or a prefix/suffix sum/product might be useful
- Traversing the array more than once (from the right)

## BigO:
Time Complexity: O(n)
Space Complexity: O(1)

## Corner cases
* n = 2, Ex: [5, 7]
* an item equal = 0, Ex: [-1, 1, 0, -3 ,3]