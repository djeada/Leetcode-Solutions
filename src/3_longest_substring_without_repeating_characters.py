class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            current_char = s[right]
            if current_char in char_index and char_index[current_char] >= left:
                # Move left past the last occurrence of current_char
                left = char_index[current_char] + 1
            # Update the most recent index of current_char
            char_index[current_char] = right
            # Update max_len if this window is larger
            max_len = max(max_len, right - left + 1)

        return max_len
