class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force time and memory O(N^2), 
        # comparing each value one at a time

        # Hash map method finds the difference between 
        # target - value. Time Complex:  O(n), memory O(n)

        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return



