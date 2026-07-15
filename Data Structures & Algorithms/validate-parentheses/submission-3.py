class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Opening Bracket tracker
        closedMatches = {")":"(", "]":"[", "}":"{"}

        for bracket in s:
            # is it a closing bracket?
            if bracket in closedMatches:
                # Is there an opening bracket to go with it?
                if stack and stack[-1] == closedMatches[bracket]:
                    # Yes, we have a pair. Remove it from the stack
                    stack.pop()
                else:
                    # It's an invalid string
                    return False
            else:
                # Bracket is opening, add to stack
                stack.append(bracket)

        # If it's empty, it's a valid string.
        if not stack:
            return True
        else:
            return False

        
            