## Data Structures

* **Key variables and data structures used in the solution**

## Overall Approach

The problem asks us to find minimum number of intervals to remove to make rest non-overlapping.

This solution involves **Sorting** the input for efficient processing.

The algorithm works by:

1. **Step 1**
   
   ```python
   def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
   ```
2. **Step 2**
   
   ```python
   for curr_start, curr_end in intervals[1:]:
            if prev_end <= curr_start:
                counter += 1
                prev_end = curr_end
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
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x[1]) # sort by second element

        prev_start, prev_end = intervals[0]
        counter = 1 # keeps track of how many intervals we keep
        
        for curr_start, curr_end in intervals[1:]:
            if prev_end <= curr_start:
                counter += 1
                prev_end = curr_end

        return len(intervals) - counter
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
