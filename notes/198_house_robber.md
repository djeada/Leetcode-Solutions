## Data Structures

* **`dp`** - Dynamic programming array to store subproblem solutions

## Overall Approach

The problem asks us to find maximum money that can be robbed without robbing adjacent houses.

This problem uses **Dynamic Programming** to build up solutions from smaller subproblems.

The algorithm works by:

1. **Step 1**
   
   ```python
   def rob(self, nums: List[int]) -> int:
        n = len(nums)
   ```
2. **Step 2**
   
   ```python
   if n == 0:
            return 0
        if n == 1:
   ```

## Complexity Analysis

* **Time Complexity**: O(n)
* **Space Complexity**: O(n)

## Key Insights

* The problem exhibits optimal substructure - optimal solution contains optimal solutions to subproblems
* Memoization avoids redundant calculations

## Source Code Analysis

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
