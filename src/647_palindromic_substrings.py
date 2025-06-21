class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.counter = 0

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                self.counter += 1
                left -= 1
                right += 1

        for center in range(2*n -1):
            left = center // 2
            right = left + (center % 2)
            expand(left, right)

        return self.counter
