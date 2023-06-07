"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

"""

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
        dict = defaultdict(list)
        for word in strs:
            dict["".join(sorted(word))].append(word)
        return dict.values()
