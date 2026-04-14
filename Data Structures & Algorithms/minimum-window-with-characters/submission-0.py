class Solution:
    def minWindow(self, search_str: str, target_str: str) -> str:
        # Quick exit for empty target
        if not target_str:
            return ""

        # Frequency maps for target characters and current window
        target_counts = {}
        window_counts = {}
        
        for char in target_str:
            target_counts[char] = 1 + target_counts.get(char, 0)

        # Track how many unique characters meet the target requirement
        met_condition_count = 0
        required_unique_chars = len(target_counts)
        
        # Result tracking: [start_index, end_index] and total length
        result_indices = [-1, -1]
        min_window_length = float("infinity")
        
        left_ptr = 0
        
        # Expand the right side of the window
        for right_ptr in range(len(search_str)):
            current_char = search_str[right_ptr]
            window_counts[current_char] = 1 + window_counts.get(current_char, 0)

            # Check if current character satisfies a target requirement
            if current_char in target_counts and window_counts[current_char] == target_counts[current_char]:
                met_condition_count += 1

            # Contract from the left once all requirements are met
            while met_condition_count == required_unique_chars:
                current_window_size = (right_ptr - left_ptr + 1)
                
                # Update smallest window found so far
                if current_window_size < min_window_length:
                    result_indices = [left_ptr, right_ptr]
                    min_window_length = current_window_size

                # Remove the left-most character and update counts
                char_at_left = search_str[left_ptr]
                window_counts[char_at_left] -= 1
                
                # If removing it breaks the requirement, decrement our counter
                if char_at_left in target_counts and window_counts[char_at_left] < target_counts[char_at_left]:
                    met_condition_count -= 1
                
                left_ptr += 1

        # Extract result from indices
        start, end = result_indices
        return search_str[start : end + 1] if min_window_length != float("infinity") else ""