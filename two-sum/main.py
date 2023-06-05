"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    #initialize a map
    map = {}
    #store the difference of target - number as the key and the index as the value
    #iterate over the list
    for index, number in enumerate(nums):
        difference = target - number
    #check to see if the difference of target - current_value is in the map

    #if not, add it and it's index to the map
        if target - difference not in map:
            map.update({difference : index})
    #if it is, return indicies of current_value and value in the map
        else:
            return [map.get(number), index]
    return [0, 0]

print(twoSum([3,2, 4], 6))
