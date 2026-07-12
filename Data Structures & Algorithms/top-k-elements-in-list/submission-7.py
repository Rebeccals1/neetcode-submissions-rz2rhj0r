class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort Method
        num_counter = {}
        freq_map = []
        
        # Make a list of empty arrays, which will eventually store our number pairs
        # i.e. freq_map = [[], [], [], [], []]  
        # Add + 1 to length to make up for the dummey index 0
        for i in range(len(nums) + 1):
            freq_map.append([])

        # Now, Count the frequency of our numbers and store it in our dictionary
        for num in nums:
            num_counter[num] = num_counter.get(num, 0) + 1

        # Next we will populate our freq_map.
        # The index will equal our Freq count and our numbers will be 
        # stored to that corresponding index number.
        # i.e. Index 2 will hold numbers with a count of 2, etc
        for num, count in num_counter.items():
            freq_map[count].append(num)

        # Now we get our results, the array is sorted in Ascending Order. Loop backwords.
        # if nums = [1,2,2,2,3,3,3], then freq_map = [[],[1],[],[3,2],[],...etc]
        # we need two loops to access numbers
        result = []
        for i in range(len(freq_map) - 1, -1, -1):
            for num in freq_map[i]:
                # Add each number
                result.append(num)
                # Stop when it reaches k in length
                if len(result) == k:
                    return result




       