class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * (2 * length)
        for i, num in enumerate(nums):
            # chained assignment in Python
            # This single line simultaneously places the current number num 
            # into two positions in the ans list
            # ans becomes [1, 2, 0, 1, 2, 0] ... 
            ans[i] = ans[i + length] = num
        return ans