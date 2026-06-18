class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
                
        for row in range(len(words)):
            for col in range(len(words[row])):
                # check if they match
                if col >= len(words) or row >= len(words[col]):
                    return False

                if words[row][col] != words[col][row]:
                    return False
        return True