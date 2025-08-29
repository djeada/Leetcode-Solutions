class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        if len(s) != len(t):
            return False
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)

        for ch in s:
            counter_s[ch] += 1

        for ch in t:
            counter_t[ch] += 1

        return counter_s == counter_t
        '''

        if len(s) != len(t):
            return False

        n = ord('z') - ord('a') + 1
        counter = [0] * n

        for ch in s:
            counter[ord(ch) - ord('a')] += 1

        for ch in t:
            counter[ord(ch) - ord('a')] -= 1

        return not any(counter)
