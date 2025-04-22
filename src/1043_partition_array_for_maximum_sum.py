class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        # max_sum_up_to[i] = best achievable sum for arr[0..i-1]
        max_sum_up_to = [0] * (n + 1)

        # Build up from the empty prefix up to the full array
        for right in range(1, n + 1):
            current_window_max = 0
            # Try all possible partition lengths ending at position right-1
            # (i.e. subarray arr[right-length .. right-1])
            for length in range(1, min(k, right) + 1):
                # Update the max in this window
                candidate_value = arr[right - length]
                if candidate_value > current_window_max:
                    current_window_max = candidate_value

                # If we take a partition of size `length` ending here,
                # total = sum up to start of this partition + length * window_max
                candidate_sum = max_sum_up_to[right - length] + length * current_window_max

                # Keep the best over all choices
                if candidate_sum > max_sum_up_to[right]:
                    max_sum_up_to[right] = candidate_sum

        # The answer for the full array is at index n
        return max_sum_up_to[n]
