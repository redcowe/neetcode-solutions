"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "[()]"
Output: true
"""

def isValid(s: str) -> bool:
    map = {")": "(", "]": "[", "}": "{"}
    stack = []

    #iterate over string
    for char in s:
        #check for if it's open para and append to stack
        if char in map.values():
            stack.append(char)
            continue
        #if it's a close paranthese and the value on top of stack equals map[char], pop
        if char in map and stack and map[char] == stack[-1]:
            stack.pop()
        else:
            return False
    return stack == []
