class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        right = left = 0

        while right < len(s) and left < len(t):
            if s[right] == t[left]:
                right += 1
            left += 1
        return right == len(s)


        
