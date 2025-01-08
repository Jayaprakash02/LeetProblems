class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {} #a:0
        max_length = -1

        for i, char in enumerate(s):
            if char in first_occurrence:

                substring_length = i - first_occurrence[char] - 1
                max_length = max(max_length, substring_length)
            else:
                first_occurrence[char] = i 

        return max_length