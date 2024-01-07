#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    target_mid_index = first_seen_index(nums, target, 0, len(nums) - 1)
    if target_mid_index == -1:
        return [-1, -1]
    starting_index = find_starting_index(nums, target, 0, target_mid_index)
    ending_index = find_ending_index(nums, target, target_mid_index, len(nums) - 1)
    return [starting_index, ending_index]

def first_seen_index(nums: List[int], target: int, l: int, r: int):
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

def find_starting_index(nums: List[int], target: int, l: int, r: int):
    i = r
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            r = m - 1
            i = m
        else:
            l = m + 1
    return i    

def find_ending_index(nums: List[int], target: int, l: int, r: int):
    i = r
    while l <= r:
        m = l + (r - l) // 2
        if nums[m] == target:
            l = m + 1
            i = m
        else:
            r = m - 1
    return i

nums = [6] * 10
target = 6
r = searchRange(nums, target)
print(r)