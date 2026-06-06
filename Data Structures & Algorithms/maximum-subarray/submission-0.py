class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algo
        maxSub, curSum = nums[0], 0

        for num in nums:
            # if the sum is negative, reset
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)

        return maxSub