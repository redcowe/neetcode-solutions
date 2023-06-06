import re
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""
def isPalindrome(s: str) -> bool:
    #if string is empty, return
    if not s: return True
    #palindrome
    #remove all non-alphanum chars from s
    #remove all white space from s
    parsed_string = ''.join(filter(str.isalnum, s)).replace(" ", "").lower()
    #designate pointer to beginning and end of array
    left_pointer = 0
    right_pointer = len(parsed_string) - 1
    #while the pointers haven't overlapped, do stuff
    while left_pointer <= right_pointer:
        #check if the values at the left and right pointers are the same
        if (parsed_string[left_pointer] == parsed_string[right_pointer]):
            #increment/decrement the pointers
            left_pointer += 1
            right_pointer -= 1
        else:
            #if values arent the same, return False
            return False
    return True

isPalindrome("random string")
