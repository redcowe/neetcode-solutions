"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

def letterCombinations(digits: str):
    if not digits: return []
    answer = set()
    map = {
        "2" : ["a","b","c"],
        "3" : ["d","e","f"],
        "4" : ["g","h","i"],
        "5" : ["j","k","l"],
        "6" : ["m","n","o"],
        "7" : ["p","q","r", "s"],
        "8" : ["t","u","v"],
        "9" : ["w","x","y", "z"]
    }

    def search(search_string: str, cur_string: list):
        if len(cur_string) == len(digits):
            answer.add("".join(cur_string))
            return
        for digit in search_string:
            cur_string.append(letter)
            search(search_string[1:], cur_string)
            cur_string.pop()
            continue


    search(digits, [])
    return list(answer)

a = letterCombinations("23")
a.sort()
print(a)
