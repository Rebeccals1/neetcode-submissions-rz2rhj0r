class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # To be valid, they must be equal length
        if len(s) != len(t):
            return False

        for char in set(s):
            # Counts how many times the character, char, appears in string s
            # If they are different, return false...
            if s.count(char) != t.count(char):
                return False
        return True
