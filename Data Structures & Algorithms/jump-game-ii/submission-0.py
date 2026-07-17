class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = right = left = 0

        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            min_jumps += 1

        return min_jumps