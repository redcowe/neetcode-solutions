"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    #create left and right pointer
    left, right = 0, 1
    result = []
    while right < len(nums):
        """
        if left + right + inverse of left + right in array
        -4 + -1 = -5 <- inverse

        """
        current_sum = nums[left] + nums[right]
        inverse = current_sum * -1
        if inverse in nums and nums[left]:
            match = [nums[left], nums[right], inverse]
            match.sort()
            if match not in result:
                result.append(match)
                left += 1
                right += 1
            else:
                left += 1
                right += 1
                continue
        else:
            left += 1
            right += 1
    return result

print(threeSum([-1,0,1,2,-1,-4]))
