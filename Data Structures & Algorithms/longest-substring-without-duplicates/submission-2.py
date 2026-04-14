class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window (Optimal)
        last_seen = {}        # Stores the last index where each character was seen
        left = 0              # Start of the sliding window
        max_length = 0        # Tracks the length of the longest valid substring found

        for right in range(len(s)):  # Move the right end of the window
            if s[right] in last_seen:
                # Move the left pointer past the last occurrence of s[right]
                left = max(last_seen[s[right]] + 1, left)
            # Update the last seen index of the current character
            last_seen[s[right]] = right
            # Update the result with the current window size
            max_length = max(max_length, right - left + 1)
        
        return max_length