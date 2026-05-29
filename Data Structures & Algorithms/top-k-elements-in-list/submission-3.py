class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create our Frequency map
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        # Create the Min-Heap - Count
        heap = []
        for num in freqMap.keys():
            heapq.heappush(heap, (freqMap[num], num) )
            # if we have too many numbers, pop the lowest count 1st
            if len(heap) > k:
                heapq.heappop(heap)
        
        results = []
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        
        return results
        