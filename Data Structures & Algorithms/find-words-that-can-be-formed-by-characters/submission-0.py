class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_bank = Counter(chars)
        result = 0

        for word in words:
            word_count = Counter(word)
            if char_bank >= word_count:
                result += len(word)
                
        return result