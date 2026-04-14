class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")": "(", "]": "[", "}": "{"}
        stack = []

        for item in s:
            if item not in dictionary:
                stack.append(item)
                continue
            if not stack or stack[-1] != dictionary[item]:
                return False
            stack.pop()
        
        return not stack # Returns a boolean value

