class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        merged_length = len(merged)
        if merged_length % 2 == 0:
            # middle values if even
            mid_index_right = merged_length // 2 - 1
            mid_index_left = merged_length // 2
            return (merged[mid_index_right] + merged[mid_index_left]) / 2
        else:
            odd_middle = merged_length // 2
            return merged[odd_middle]
        

        