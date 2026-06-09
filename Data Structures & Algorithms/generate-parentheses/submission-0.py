class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        stack = []

        def backtrack(openNum, closedNum):
            if openNum == closedNum == n:
                results.append("".join(stack))
                return
            if openNum < n:
                stack.append("(")
                backtrack(openNum + 1, closedNum)
                stack.pop()
            if openNum > closedNum:
                stack.append(")")
                backtrack(openNum, closedNum + 1)
                stack.pop()
            
        backtrack(0,0)
        return results
            