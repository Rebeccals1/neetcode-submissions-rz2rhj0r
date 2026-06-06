class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k-1])
        count = 0
        arrLen = len(arr)

        for left in range(arrLen - k + 1):
            total += arr[left + k - 1]
            
            if (total / k) >= threshold:
                count += 1

            total -= arr[left]
            
        return count

