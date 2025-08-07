## Data Structures

* **`result`** - Stores the final answer/output of the algorithm
* **`dp`** - Dynamic programming array to store subproblem solutions

## Overall Approach

The problem asks us to count unique paths from top-left to bottom-right in grid.

This problem uses **Dynamic Programming** to build up solutions from smaller subproblems.

The algorithm works by:

1. **Step 1**
   
   ```python
   def uniquePaths(self, m: int, n: int) -> int:
        '''
        N = m + n - 2
   ```
2. **Step 2**
   
   ```python
   for i in range(1, 1 + k):
            result = result * (N - k + i) // i

        return result
   ```

## Complexity Analysis

* **Time Complexity**: O(n²)
* **Space Complexity**: O(n²)

## Key Insights

* The problem exhibits optimal substructure - optimal solution contains optimal solutions to subproblems
* Memoization avoids redundant calculations

## Source Code Analysis

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        N = m + n - 2
        k = min(n-1, m-1)
        result = 1

        for i in range(1, 1 + k):
            result = result * (N - k + i) // i

        return result
        '''

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
