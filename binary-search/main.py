"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [0, 3, 5, 9, 12, 14, 20], target = 14
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) -1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1
        else:
            return mid
    return -1

print(search([0, 3, 5, 9, 12, 14, 20], 9))
