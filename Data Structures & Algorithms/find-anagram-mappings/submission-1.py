class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        positons = {}
        
        # Creates position = {number key: index value}
        for i in range(len(nums2)):
            positons[nums2[i]] = i
        
        results = []
        for i in range(len(nums1)):
            index = positons[nums1[i]]
            results.append(index)

        return results