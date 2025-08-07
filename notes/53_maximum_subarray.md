## Data Structures

* **Key variables and data structures used in the solution**

## Overall Approach

The problem asks us to find the contiguous subarray with the largest sum.

This solution uses an efficient approach to solve the problem.

The algorithm works by:

1. **Step 1**
   
   ```python
   def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
   ```
2. **Step 2**
   
   ```python
   for num in nums[1:]:
            if curr_sum < 0:
                curr_sum = num
            else:
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
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum, best_sum = nums[0], nums[0]

        for num in nums[1:]:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num

            if curr_sum > best_sum:
                best_sum = curr_sum

        return best_sum
```

## Related Problems

* Similar problems involving the same algorithmic techniques
* Problems with related data structures or approaches
