class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums) # remove duplicates + O(1) lookups
        longest_streak = 0

        for curr_num in numbers:
            # check if this is the START of a sequence
            if (curr_num - 1) not in numbers:

                current_streak_length = 1

                # keep checking next numbers in sequence
                while (curr_num + current_streak_length) in numbers:
                    current_streak_length += 1

                # update longest streak found so far
                longest_streak = max(longest_streak, current_streak_length)

        return longest_streak