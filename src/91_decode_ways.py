class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge cases
        if not s or s[0] == '0':
            return 0

        # ways_two_back = dp[i-2], ways_one_back = dp[i-1]
        ways_two_back, ways_one_back = 1, 1

        for idx in range(1, len(s)):
            ways_current = 0

            # Single-digit decode
            if s[idx] != '0':
                ways_current += ways_one_back

            # Two-digit decode for prev char + curr char
            two_digit = int(s[idx-1:idx+1])
            if 10 <= two_digit <= 26: # max letter is Z -> 26
                ways_current += ways_two_back

            # Slide window
            ways_two_back, ways_one_back = ways_one_back, ways_current

            # Early exit if no valid decoding so far
            if ways_one_back == 0:
                return 0

        return ways_one_back
