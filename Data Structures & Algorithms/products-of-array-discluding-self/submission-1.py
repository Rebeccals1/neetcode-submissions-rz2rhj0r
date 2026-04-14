class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize the result array with all values set to 1
        results = [1] * (len(nums))

        # First pass (left to right)
        prefix = 1
        for i in range(len(nums)):
            # set product of all elements to the left
            results[i] = prefix
            # Update Prefix
            prefix *= nums[i]
        
        # Second pass (right to left)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # Multiply results by postfix (product of all elements to the right)
            results[i] *= postfix
            # Update postfix
            postfix *= nums[i]

        return results