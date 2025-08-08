## Data Structures

**Inputs:**

* `s`: source string (length $n$).
* `t`: target multiset of characters (length $m$).

**Auxiliary variables:**

* `counter`: map $c \mapsto \text{deficit}(c)$. Initialized with counts from $t$.

  * Interpretation: positive → still needed; zero → exactly satisfied; negative → surplus in window.
* `missing`: total outstanding characters still needed (sum of positive deficits).
* `left`, `right`: window boundaries on `s` (inclusive `left`, inclusive `right` while scanning).
* `best_left`, `best_right`: endpoints of the best (shortest) valid window found so far.

## Overall Approach

Use a **sliding window** with two pointers:

1. **Expand right**: include `s[right]`. If that character was needed (`counter[char] > 0`), decrease `missing`. Always decrement `counter[char]` (surpluses go negative).
2. **When covered** (`missing == 0`): the current window contains all of `t`.

 * **Shrink left** while the leftmost character is surplus (`counter[s[left]] < 0`), incrementing its count back and moving `left` rightward.
 * **Record** this minimal window.
 * **Kick out** the leftmost required character (increment its count, move `left`, and increment `missing`) to search for the next candidate window.

Window optimality comes from always trimming surplus before recording.

```mermaid
flowchart TD
  A[Init counter from t; missing = |t|; left=0; best=None] --> B[for right in 0..n-1]
  B --> C[Include s[right]: if counter>0 then missing-- ; counter--]
  C --> D{missing == 0?}
  D -->|No| B
  D -->|Yes| E[While counter[s[left]] < 0: counter++ ; left++]
  E --> F[Update best with [left, right]]
  F --> G[Prepare next: counter[s[left]]++ ; left++ ; missing++]
  G --> B
```

## Invariants

* At any time, for each character $c$:

$$
\text{counter}(c) = \text{needed}(c) - \text{in\_window}(c).
$$

* `missing` equals $\sum_{c} \max(0, \text{counter}(c))$.
* `missing == 0` ⇔ window covers all characters of `t` (with multiplicity).

## Complexity Analysis

* **Time:** $O(n)$. Each index enters and leaves the window at most once; all hash ops are $O(1)$ amortized.
* **Space:** $O(\Sigma)$, size of the character alphabet used in `t` (and in practice bounded by the character set).
76_minimum_window_substring
