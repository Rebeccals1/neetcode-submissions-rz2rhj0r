class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set(nums)
        # If there are no duplicates in nums, then the number 
        # of unique elements will be equal to the total number 
        # of elements (i.e., len(set(nums)) == len(nums)). 
        # In this case, the condition len(set(nums)) < len(nums) 
        # will be False.
        result = len(num_set) < len(nums)
        return result