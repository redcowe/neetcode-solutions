"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""
def topKFrequent(nums: list[int], k: int):
    map = dict()
    answer = []
    for value in nums:
        if value not in map:
            map[value] = 1
        else:
            map[value] += 1

    while len(answer) < k:
        most_frequent = max(map, key=map.get)
        answer.append(most_frequent)
        del map[most_frequent]

    return answer

print(topKFrequent([1,1,1,2,2,3], 2))
