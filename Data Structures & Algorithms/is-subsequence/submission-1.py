class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two Pointers
        '''
        Algorithm
        1. Initialize pointers i = 0 and j = 0.
        2. While i < len(s) and j < len(t):
                If s[i] == t[j], increment i.
                Always increment j.
        3. Return i == len(s).
        '''
        right = left = 0

        while right < len(s) and left < len(t):
            if s[right] == t[left]:
                right += 1
            left += 1
        return right == len(s)


        
