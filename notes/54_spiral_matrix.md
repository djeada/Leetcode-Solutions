## Data Structures

* **`result`** - Stores the final answer/output of the algorithm

## Overall Approach

The problem asks us to return all elements of matrix in spiral order.

This solution uses an efficient approach to solve the problem.

The algorithm works by:

1. **Step 1**
   
   ```python
   def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
   ```
2. **Step 2**
   
   ```python
   while matrix:
            row = matrix.pop(0)
            result.extend(row)
   ```

## Complexity Analysis

* **Time Complexity**: O(n)
* **Space Complexity**: O(1)

## Key Insights

* Consider edge cases and boundary conditions
* The algorithm handles the problem constraints efficiently

## Source Code Analysis

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        while matrix:
            row = matrix.pop(0)
            result.extend(row)

            # ccw 90 rotation
            matrix = [
                row for row in 
                reversed(list(zip(*matrix)))
            ]

        return result
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
