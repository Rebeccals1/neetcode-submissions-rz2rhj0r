class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            # count the letters in the word
            for letter in word:
                count[ord(letter) - ord('a')] += 1
            # store the paired words
            result[tuple(count)].append(word)

        return list(result.values())