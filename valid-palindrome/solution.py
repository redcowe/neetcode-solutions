import re

def isPalindrome(s: str) -> bool:
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left_p = 0
        right_p = len(s) - 1

        while left_p < right_p:
            print(left_p, right_p)
            if clean_s[left_p] != clean_s[right_p]:
                return False
            left_p += 1
            right_p -= 1
        return True

print(isPalindrome("abcba"))