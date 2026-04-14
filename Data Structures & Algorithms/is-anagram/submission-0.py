class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # They have to be the same length to be an anagram
        if len(s) != len(t): 
            return False
        
        # Time Complex O(s + t), size of s and t
        countS = {}
        countT = {}

        for i in range(len(s)):
            # countS[s[i]] += 1 will give an error because you cant add to
            # an empty dictionary (countS)
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0) # zero is default value if empty
        for c in countS:
            if countS[c] != countT.get(c, 0): 
                return False
        
        return True
            