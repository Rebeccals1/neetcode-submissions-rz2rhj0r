class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        curr_sum = 0

        left = 0
        right = len(numbers) - 1

        while left < right:
            curr_sum = numbers[right] + numbers[left]

            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
