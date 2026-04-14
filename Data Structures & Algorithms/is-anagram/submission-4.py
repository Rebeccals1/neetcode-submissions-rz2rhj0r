class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        hashy = {}
        

        for char in s:
            if char in hashmap:
                hashmap[char] = hashmap[char] + 1
            else:
                hashmap[char] = 1
            
        for char in t:
            if char in hashy:
                hashy[char] = hashy[char] + 1
            else:
                hashy[char] = 1

        return hashmap == hashy
            

