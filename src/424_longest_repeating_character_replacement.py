class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        L = 0
        most_frequent = 0
        result = 0

        for R, current_char in enumerate(s):
            count[current_char] += 1
            most_frequent = max(most_frequent, count[current_char])
            while R - L + 1 - most_frequent > k:
                count[s[L]] -= 1
                L += 1

            result = max(result, R - L + 1)

        return result
