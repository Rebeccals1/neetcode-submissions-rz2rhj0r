class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # move right to mid (minimum is on the left).
                right = mid
            else:
                # move left to mid + 1 (minimum is on the right)
                left = mid + 1
                
        return nums[left]