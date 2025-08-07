## Data Structures

* **`result`** - Stores the final answer/output of the algorithm

## Overall Approach

The problem asks us to group strings that are anagrams of each other.

This solution uses **Hash Tables** for O(1) lookup and storage.

The algorithm works by:

1. **Step 1**
   
   ```python
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result: defaultdict = defaultdict(list)
   ```
2. **Step 2**
   
   ```python
   for word in strs:
            # --- Histogram count approach (linear time per word) ---
            # histo = [0] * 26
            # for ch in word:
   ```

## Complexity Analysis

* **Time Complexity**: O(n log n)
* **Space Complexity**: O(1)

## Key Insights

* Hash table provides O(1) average lookup time

## Source Code Analysis

```python
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
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
