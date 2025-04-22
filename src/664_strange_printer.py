class Solution:
    def strangePrinter(self, s: str) -> int:
        # 1) Collapse consecutive identical letters into a list `chars`
        #    since printing "aaa" is the same as printing "a".
        chars = []
        for ch in s:
            if not chars or chars[-1] != ch:
                chars.append(ch)
        n = len(chars)
        if n == 0:
            return 0

        # 2) min_prints[i][j] = minimum printer turns needed to print chars[i..j]
        min_prints = [[0] * n for _ in range(n)]

        # Base case: a single character always takes 1 turn
        for start in range(n):
            min_prints[start][start] = 1

        # Fill DP for all substring lengths from 2 up to n
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                # Worst case: print chars[start..end-1], then one more turn for chars[end]
                best_for_range = min_prints[start][end - 1] + 1

                # Try merging the final character's print with any matching char in [start..end-1]
                for mid in range(start, end):
                    if chars[mid] == chars[end]:
                        # If chars[mid] == chars[end], the turn that prints at `mid`
                        # can extend to cover `end` as well
                        without_last = min_prints[start][mid]
                        middle_segment = min_prints[mid + 1][end - 1] if mid + 1 <= end - 1 else 0
                        candidate = without_last + middle_segment
                        if candidate < best_for_range:
                            best_for_range = candidate

                min_prints[start][end] = best_for_range

        # The answer for the whole compressed string is min_prints[0][n-1]
        return min_prints[0][n-1]
