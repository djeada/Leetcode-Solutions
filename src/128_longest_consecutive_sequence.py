from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for x in num_set:
            # only start counting if x is the beginning of a sequence
            if x - 1 not in num_set:
                y = x + 1
                while y in num_set:
                    y += 1
                # y is now one past the end of the run [x … y−1]
                longest = max(longest, y - x)

        return longest
