class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sorted_nums = sorted(list(set(nums)))
        max_counter = 0
        counter = 0
        left = 0
        right = 1

        while right < len(sorted_nums):
            if (sorted_nums[left] + 1) == sorted_nums[right]:
                counter += 1
            else:
                max_counter = max(max_counter, counter)
                counter = 0
            right += 1
            left += 1
        return max(max_counter, counter) + 1