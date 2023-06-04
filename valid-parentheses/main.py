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
"""

# Initial solution that doesn't pass is below:
def isValid(s: str) -> bool:
    #if string is empty to start just return false
    if not s: return False
    parentheses_map = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    if len(s) == 1: return False
    if len(s) % 2 != 0: return False
    while s != "":
        current_char = s[0]
        if s == "": return True
        if current_char not in parentheses_map.values(): return False
        if parentheses_map.get(s[1]) == current_char:
            s = s[2:]
        else: return False
    return True

# valid_chars = ['a', 'b', 'c']
# test_char = "a"
# if test_char not in valid_chars: print("not valid")

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))


# Passing solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack
