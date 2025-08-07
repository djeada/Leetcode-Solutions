## Data Structures

* **Key variables and data structures used in the solution**

## Overall Approach

The problem asks us to merge all overlapping intervals.

This solution involves **Sorting** the input for efficient processing.

The algorithm works by:

1. **Step 1**
   
   ```python
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return list()
   ```
2. **Step 2**
   
   ```python
   for pair in intervals[1:]:
            # overlap
            if merged[-1][1] >= pair[0]:
                if pair[1] > merged[-1][1]:
   ```

## Complexity Analysis

* **Time Complexity**: O(n log n)
* **Space Complexity**: O(1)

## Key Insights

* Consider edge cases and boundary conditions
* The algorithm handles the problem constraints efficiently

## Source Code Analysis

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return list()

        intervals.sort(key=lambda pair: pair[0])
        merged = [intervals[0]]
        
        for pair in intervals[1:]:
            # overlap
            if merged[-1][1] >= pair[0]:
                if pair[1] > merged[-1][1]:
                    merged[-1][1] = pair[1]
            # no overlap
            else:
                merged.append(pair)

        return merged
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
