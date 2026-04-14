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
            # move right until we find '#'
            while s[pointer] != '#':
                pointer += 1 
            length = int(s[index:pointer]) # find the number (length of word)
            index = pointer + 1 # Move to the starting of the word
            pointer = index + length # Move pointer to the end of word (index + length)
            result.append(s[index:pointer]) # Extract and add word to array
            index = pointer # move index to the next word
        
        return result
