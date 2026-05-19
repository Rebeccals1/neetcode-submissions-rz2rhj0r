class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def dfs(index):
            # Base Case
            if index >= len(s):
                result.append(part.copy())
                return

            # Check every possible substring
            for j in range(index, len(s)):
                if self.isPali(s,index, j):
                    part.append(s[index:j + 1])
                    dfs(j + 1)
                    part.pop()
            
        dfs(0)
        return result
    
    def isPali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True
