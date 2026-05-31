class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        counter = 0
        
        for i in range(len(ans)):
            ans[i] = nums[counter]
            counter += 1
            if counter == len(nums):
                counter = 0
        
        return ans
        

        