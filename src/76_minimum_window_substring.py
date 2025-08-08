from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        missing = len(t)
        best_left, best_right = 0, 0
        left = 0

        for right, character in enumerate(s):
            # just moving the right pointer
            if counter[character] > 0:
                missing -= 1
            counter[character] -= 1

            # it's to move the left pointer, we have found
            # all the necessary characters
            if missing == 0:
                while left <= right and counter[s[left]] < 0:
                    counter[s[left]] += 1
                    left += 1

                # we can try to update the global best left and right
                if best_right == 0 or right + 1 - left < best_right - best_left:
                    best_left, best_right = left, right + 1

                # now we are looking for a potenatial new window
                counter[s[left]] += 1
                left += 1
                missing += 1

        return s[best_left: best_right]
