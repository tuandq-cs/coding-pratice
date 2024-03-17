from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 1 <= nums <= 10^4
        ans = [-1] * len(nums)
        # build monoStack for next greater element for last index
        # go from [len(nums) - 2 -> 0]
        monoStack = []
        i = len(nums) - 2
        while (i >= 0):
            # insert the current element to the stack
            # pop those elements has num <= nums[i]
            while (len(monoStack) > 0 and nums[monoStack[-1]] <= nums[i]):
                monoStack.pop()
            monoStack.append(i)
            i -= 1
        
        # now we has monoStack for the last element
        # I need to loop for eac element to find the next greater number
        i = len(nums) - 1
        while (i >= 0):
            while (len(monoStack) > 0 and nums[monoStack[-1]] <= nums[i]):
                monoStack.pop()
            if len(monoStack) > 0:
                ans[i] = nums[monoStack[-1]]
            monoStack.append(i)
            i -= 1
        return ans