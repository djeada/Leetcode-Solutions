## Data Structures

* **`left, right`** - Two pointers for sliding window or binary search

## Overall Approach

The problem asks us to solve the isnert interval problem.

This solution uses the **Two Pointers** technique to efficiently traverse the data.

The algorithm works by:

1. **Step 1**
   
   ```python
   def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left = [
   ```
2. **Step 2**
   
   ```python
   interval for interval in intervals if 
            interval[1] < newInterval[0]
        ]
   ```

## Complexity Analysis

* **Time Complexity**: O(n)
* **Space Complexity**: O(1)

## Key Insights

* Two pointers technique reduces time complexity from O(n²) to O(n)

## Source Code Analysis

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left = [
            interval for interval in intervals if 
            interval[1] < newInterval[0]
        ]

        right = [
            interval for interval in intervals if 
            interval[0] > newInterval[1]
        ]

        middle = [
            interval for interval in intervals if 
            not (
                interval[1] < newInterval[0] 
                or interval[0] > newInterval[1]
            )
        ] + [newInterval]

        middle = [
            min(interval[0] for interval in middle),
            max(interval[1] for interval in middle)
        ]

        return left + [middle] + right
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
