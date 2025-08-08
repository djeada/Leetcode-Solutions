## Data Structures

**Inputs:**

* `intervals`: list of closed (or half-open) intervals $[s_i, e_i]$ on the line.

**Auxiliary variables:**

* `prev_end`: end of the last **kept** interval in the greedy sweep.
* `keep`: number of kept, non-overlapping intervals (answer will be $n-\text{keep}$).

## Overall Approach

Minimizing removals is equivalent to **maximizing the number of non-overlapping intervals kept**. That is the classic **interval scheduling** problem: sort by earliest finishing time and greedily keep any interval that doesn’t overlap the last kept one.

Let intervals be sorted by nondecreasing end $e$. Sweep left→right:

* If the next start $s$ satisfies $s \ge \text{prev\_end}$, **keep** it and set $\text{prev\_end} \leftarrow e$.
* Otherwise, **skip** it (conceptually “remove” it).

The number to remove is $\;n - \text{keep}$.

```mermaid
flowchart TD
  A[Sort intervals by end time] --> B[Initialize prev_end = end of first, keep = 1]
  B --> C[For each (s,e) in remaining intervals]
  C --> D{s ≥ prev_end?}
  D -->|Yes| E[keep += 1; prev_end = e]
  D -->|No| F[skip (remove) this one]
  E --> C
  F --> C
  C --> G[After loop, answer = n - keep]
```

## Why This Greedy Is Optimal (Sketch)

* **Greedy choice property:** Among all intervals that could be taken next, picking the one with the **earliest end** leaves the most room for the rest, never reducing the number we can still keep.
* **Exchange argument:** Given any optimal solution, if its first kept interval doesn’t end as early as the greedy one, swap it with the greedy choice. The schedule stays feasible and no worse in size. Repeating this yields a schedule identical to the greedy one, so greedy is optimal.

## Example

Intervals: $[1,3], [2,4], [3,5], [0,2]$.
Sort by end: $[0,2], [1,3], [3,5], [2,4]$.

* Keep $[0,2]$ → `prev_end=2`, `keep=1`.
* $[1,3]$: $1<2$ → skip.
* $[3,5]$: $3\ge2$ → keep → `prev_end=5`, `keep=2`.
* $[2,4]$: $2<5$ → skip.
  Kept $=2$ ⇒ removals $=4-2=2$.

*(If the problem treats touching intervals as non-overlapping, use $s \ge \text{prev\_end}$. If it requires a gap, use $s > \text{prev\_end}$. Many formulations implicitly use half-open $[s,e)$, making equality safe.)*

## Complexity Analysis

* **Time:** sorting dominates → $O(n\log n)$.
* **Space:** $O(1)$ extra (in-place scan after sorting).
