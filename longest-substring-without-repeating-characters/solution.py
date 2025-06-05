def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0
        # iterate over each value in the string
        tempString = ""
        for letter in s:
        # continue to add values to a temporary string until a letter present in the string appears again
            if letter not in tempString:
                tempString += letter
            else:
                if len(tempString) > longestSubstring:
                    longestSubstring = len(tempString)
                tempString = letter        
        return longestSubstring
                        

print(lengthOfLongestSubstring(None, "c"))  # Example usage