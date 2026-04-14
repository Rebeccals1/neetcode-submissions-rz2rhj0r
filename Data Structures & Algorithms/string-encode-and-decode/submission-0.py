class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        index = 0

        while index < len(s):
            pointer = index
            # Keep going until you find the next word length (number)
            while s[pointer] != '#':
                pointer += 1 
            length = int(s[index:pointer]) # Length of the word
            index = pointer + 1 # Move to the starting of the word
            pointer = index + length # Get the whole word
            result.append(s[index:pointer]) # add to our array
            index = pointer # move index to the next word
        
        return result
