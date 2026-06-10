class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                indexNum = nums2.index(nums1[i])
                result.append(indexNum)

        return result