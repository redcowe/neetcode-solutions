"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
"""

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    #input = [73,74,75,71,69,72,76,73]
    #stack = [[temp, index]]
    stack = [0] * len(temperatures)
    result = []
    for index, temp in enumerate(temperatures):
        stack.append([temp, index])
        while stack:

            return
        return

    return result
    #
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
