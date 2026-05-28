class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S_count = {}
        T_count = {}

        if len(t) != len(s):
            return False
        
        for i in range(len(s)):
            S_count[s[i]] = S_count.get(s[i], 0) + 1
            T_count[t[i]] = T_count.get(t[i], 0) + 1
        
        return S_count == T_count



