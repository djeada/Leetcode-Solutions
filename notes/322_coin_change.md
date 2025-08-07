## Data Structures

* **`dp`** - Dynamic programming array to store subproblem solutions

## Overall Approach

The problem asks us to find minimum number of coins needed to make up a given amount.

This problem uses **Dynamic Programming** to build up solutions from smaller subproblems.

The algorithm works by:

1. **Step 1**
   
   ```python
   def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [0] + [INF] * amount
   ```
2. **Step 2**
   
   ```python
   for i in range(1, amount + 1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
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
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1
        dp = [0] + [INF] * amount

        for i in range(1, amount + 1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
                
        return dp[amount] if dp[amount] != INF else -1
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
