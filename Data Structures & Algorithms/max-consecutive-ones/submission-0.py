class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        freq = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
                freq = 0
            else:
                freq += 1
                
            if freq > best:
                best = freq

        return best



        


        