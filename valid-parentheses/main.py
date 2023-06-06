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
    for char in s:
        #if char is an open parantheses, push it onto stack
        if char not in map:
            stack.append(char)
            continue
        #if stack is empty(stack is empty is if s is empty or char is a close parantheses) or the last value in the stack doesn't have a key in the map, return false
        if not stack or stack[-1] != map[char]:
            return False
        stack.pop()
    return not stack
