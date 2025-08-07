## Data Structures

* **`matrix`**: an $n\times n$ 2D list, modified in place.

* **Loop indices**
* `i`, `j`: integers ranging over row and column indices.

## Overall Approach

We perform a **90° clockwise** rotation by two simple, in-place transformations:

1. **Transpose** the matrix across its main diagonal: swap $\text{matrix}[i][j]$ with $\text{matrix}[j][i]$ for $j>i$.
2. **Reverse** each row horizontally.

Together, these steps map the element at $(r,c)$ to its rotated position $(c,\,n-1-r)$.

```mermaid
flowchart TD
  A[Start: read n = len(matrix)] --> B[Transpose]
  B --> C[For i in 0…n-1, for j in i+1…n-1: swap (i,j) ↔ (j,i)]
  C --> D[Reverse Rows]
  D --> E[For each row: row.reverse()]
  E --> F[Done – matrix rotated]
```

## Complexity Analysis

**Time Complexity:**

* **Transpose:** visits each off-diagonal pair once → $\sum_{i=0}^{n-1}(n-1-i)=\frac{n(n-1)}{2}$ swaps → $O(n^2)$.
* **Row reversal:** each of the $n$ rows of length $n$ reversed in $O(n)$ → $O(n^2)$.
* **Overall:** $O(n^2)$.

**Space Complexity:**

* **In place:** $O(1)$ extra space beyond the input.

