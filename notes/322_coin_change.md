## Data Structures

**Inputs:**

* `coins`: set of coin denominations $\{c_j\}$.
* `amount`: target sum $A$.

**Auxiliary Variables:**

* `dp`: array of length $A+1$, where

  $$
    dp[i] = \text{minimum coins needed to make sum }i,
  $$

  with $dp[0]=0$ and all other entries initialized to a large “infinite” value.

## Overall Approach

We exploit the **optimal substructure**: the best way to form amount $i$ is to take one coin $c_j$ and then optimally form $i - c_j$. Thus each state builds on previously solved smaller amounts.

```mermaid
flowchart TD
  A[Start: define INF = A+1, dp[0]=0, dp[1…A]=INF] --> B[For i = 1 to A]
  B --> C[For each coin c in coins]
  C --> D{if i ≥ c?}
  D -->|Yes| E[dp[i] ← min(dp[i], dp[i−c] + 1)]
  D -->|No| F[skip]
  E --> G{more coins?}
  G -->|Yes| C
  G -->|No| H{more i?}
  H -->|Yes| B
  H -->|No| I[Return dp[A] unless INF → −1]
  I --> J[Done]
```

### I. Initialization

* Set an upper bound “infinity” as

  $$
    \text{INF} = A + 1.
  $$
* Create `dp` so that

  $$
    dp[0] = 0,\quad
    dp[i] = \text{INF}\quad\text{for }i=1,\dots,A.
  $$

### II. Recurrence Relation

For each sub-amount $i$ from $1$ to $A$, and for each coin $c_j$:

1. If $i - c_j \ge 0$, a valid subproblem exists.
2. The candidate solution using coin $c_j$ is

   $$
     1 + dp[i - c_j].
   $$
3. Take the minimum over all denominations to update

   $$
     dp[i] \;=\; \min_j\bigl(dp[i],\;1 + dp[i - c_j]\bigr).
   $$

This ensures that by the time we reach $i$, all smaller amounts have been optimally solved.

## Example

Let `coins = [1, 3, 4]` and `amount = 6`. Then stepwise:

|      $i$     |  0  |  1  |  2  |  3  |  4  |  5  |  6  |
| :----------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| dp\[i] start |  0  |  ∞  |  ∞  |  ∞  |  ∞  |  ∞  |  ∞  |
|    using 1   |     |  1  |  2  |  3  |  4  |  5  |  6  |
|    using 3   |     |     |     |  1  |     |  2  |  3  |
|    using 4   |     |     |     |     |  1  |     |  2  |
|   **final**  |  0  |  1  |  2  |  1  |  1  |  2  |  2  |

* For $i=3$: best is one 3-coin → $dp[3]=1$.
* For $i=4$: best is one 4-coin → $dp[4]=1$.
* For $i=5$: either $dp[5]=dp[5-4]+1=2$ or $dp[5]=dp[5-3]+1=dp[2]+1=3$, so $2$.
* For $i=6$: either $dp[6]=dp[6-4]+1=dp[2]+1=3$ or $dp[6]=dp[6-3]+1=dp[3]+1=2$, so $2$.

## Complexity

* **Time:**
  Outer loop runs $A$ times; inner loop iterates over $\lvert\text{coins}\rvert$.

  $$
    O(A \times \lvert\text{coins}\rvert).
  $$
* **Space:**

  $$
    O(A)
  $$

  for the `dp` array.
