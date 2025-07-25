from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: defaultdict = defaultdict(list)

        for word in strs:
            # --- Histogram count approach (linear time per word) ---
            # histo = [0] * 26
            # for ch in word:
            #     histo[ord(ch) - ord('a')] += 1
            # # bytes() is C‑level and fast to hash
            # result[bytes(histo)].append(word)

            # --- Sort & join approach (O(k log k) per word) ---
            key = "".join(sorted(word))
            result[key].append(word)

        return list(result.values())
