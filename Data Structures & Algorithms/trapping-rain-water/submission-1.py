class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        result = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                # Update the max first
                leftMax = max(leftMax, height[left])
                # Then add the trapped water (which will be 0 if height[left] is the new max)
                result += leftMax - height[left]
            else:
                right -= 1
                # Update the max first
                rightMax = max(rightMax, height[right])
                # Then add the trapped water
                result += rightMax - height[right]

        return result
