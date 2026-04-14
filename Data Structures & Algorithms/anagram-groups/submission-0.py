class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for letter in strs:
            count = [0] * 26 # for 26 letters in alphabet

            for s in letter:
                count[ord(s) - ord('a')] += 1
            
            res[tuple(count)].append(letter)
        return list(res.values())


        