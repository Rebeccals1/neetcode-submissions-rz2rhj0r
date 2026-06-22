class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        for word in strs:
            # Reset letter count
            letter_count = [0] * 26
            # Count the letters in the word
            for letter in word:
                letter_count[ord(letter) - ord("a")] += 1
            # Make letter count our key and append the word to our list
            word_dict[tuple(letter_count)].append(word)
        # Return our lists
        return list(word_dict.values())
            
