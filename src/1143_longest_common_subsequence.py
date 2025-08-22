class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i, ch1 in enumerate(text1, 1):
            row = dp[i]
            prev_row = dp[i - 1]
            for j, ch2 in enumerate(text2, 1):
                if ch1 == ch2:
                    row[j] = prev_row[j - 1] + 1
                else:
                    row[j] = max(prev_row[j], row[j - 1])
                

        return dp[m][n]
