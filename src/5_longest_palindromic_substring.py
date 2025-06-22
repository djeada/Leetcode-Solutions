class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ""

        # return the longest palindromic substring
        def expand(left, right):

            # two cases, one for odd and one for even
            if left == right:
                _result = s[left]
            else:
                if s[left] != s[right]:
                    return ""
                _result = s[left] + s[right]
            left -= 1
            right += 1

            while left >= 0 and right < n and s[left] == s[right]:
                _result = s[left] + _result + s[right]
                left -= 1
                right += 1

            return _result

        for center in range(2*n - 1):
            left = center // 2
            right = left + (center % 2)
            substring = expand(left, right) 
            if len(substring) > len(result):
                result = substring

        return result
        
