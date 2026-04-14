class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # right point to the beginning of the array
        # left point to the end of the array (total length)
        # result will be a new empty array

        # loop through the range(len(array))
        #   if right + left == target
        #       result append index into new array
        #       

        # return new array
        hash = {}
        
        for i, num in enumerate(nums):
            if target - num in hash:
                return [hash[target - num], i]
            hash[num] = i
        return None

            

