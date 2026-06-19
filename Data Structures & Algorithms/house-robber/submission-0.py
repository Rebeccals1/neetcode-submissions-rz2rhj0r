class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic Programming
        rob1 = 0
        rob2 = 0

        for num in nums:
            current = max(rob2, num + rob1)
            rob1 = rob2
            rob2 = current
        
        return rob2

        
