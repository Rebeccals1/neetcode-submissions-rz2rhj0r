class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        max_frequency = 0
        
        for right in range(len(s)):
            # Update frequency map and max_frequency
            count[s[right]] = 1 + count.get(s[right], 0)
            max_frequency = max(max_frequency, count[s[right]])

            # Check if current window is valid
            # (right - left + 1) is the current window size
            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            # Update result with the now-valid window size
            result = max(result, right - left + 1)
        
        return result
        