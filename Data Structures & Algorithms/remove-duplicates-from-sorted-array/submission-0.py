class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_list = sorted(list(set(nums)))
        
        for i in range(len(unique_list)):
            nums[i] = unique_list[i]
        return len(unique_list)

        
