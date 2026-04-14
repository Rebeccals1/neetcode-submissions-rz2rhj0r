class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        # Make an Empty 2D Array with same length as nums 
        # num_freq = [[], [], [], [], []]
        num_freq = [[] for i in range(len(nums)+1)] 

        # Count how many times the value shows up in nums
        for n in nums: 
            # use get() to count values, if it doesn't exist assign it 0
            counter[n] = 1 + counter.get(n,0)

        # for every number (n) and count (c), I want to make a hashmap that makes c the index and n it's value
        for n, c in counter.items():
            num_freq[c].append(n)
        
        results = []
        # -1 means descending order
        # range(start, stop, step)
        for i in range(len(num_freq) - 1, 0 , -1):
            for n in num_freq[i]:
                results.append(n)
                if len(results) == k:
                    return results