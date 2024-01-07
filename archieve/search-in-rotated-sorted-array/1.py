# https://leetcode.com/problems/search-in-rotated-sorted-array/

from ctypes.wintypes import tagRECT
from typing import List



def search(nums: List[int], target: int) -> int:
    rotated_index = find_rotated_index(nums)

    if rotated_index != -1:
        target_index_1 = binary_search(nums, target, 0, rotated_index-1)
        target_index_2 = binary_search(nums, target, rotated_index, len(nums) - 1)
        target_index = target_index_1 if target_index_1 != -1 else target_index_2
    else:
        target_index =  binary_search(nums, target, 0, len(nums) - 1)
    return target_index

def find_rotated_index(nums: List[int]):
    rotated_index = -1
    l = 0
    r = len(nums) - 1
    first_item = nums[0]
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] < first_item:
            r = m - 1
            rotated_index = m
        else:
            l = m + 1
    return rotated_index
    
def binary_search(nums: List[int], target: int, l: int, r: int):
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

# [4,5,6,7,0,1,2], target = 0
nums = [4,5,6,7,0,1,2]
# nums = [1,2,4,5,6,7,0]
# nums = [3,1]

target = 7
r = search(nums, target)
print(r)
