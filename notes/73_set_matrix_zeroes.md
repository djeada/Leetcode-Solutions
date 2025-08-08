## Data Structures

**Inputs:**

* `matrix`: an $m\times n$ grid of integers.

**Auxiliary:**

* `marked_rows`: length-$m$ boolean array where `marked_rows[i] = True` iff row $i$ contains at least one 0.
* `marked_cols`: length-$n$ boolean array where `marked_cols[j] = True` iff column $j$ contains at least one 0.

## Overall Approach

Think of the solution as computing two sets:

$$
R=\{i\mid \exists j:\; \text{matrix}[i][j]=0\},\qquad
C=\{j\mid \exists i:\; \text{matrix}[i][j]=0\}.
$$

The final matrix should satisfy

$$
\text{matrix}[i][j]=0 \quad \text{iff} \quad i\in R \;\; \text{or} \;\; j\in C.
$$

To achieve this without letting newly written zeros “infect” other rows/cols, we do it in **two passes**:

1. **Scan pass (read-only):** identify $R$ and $C$ by looking for original zeros and marking the corresponding row/column.
2. **Write pass:** for each cell $(i,j)$, set it to zero if `marked_rows[i]` or `marked_cols[j]` is true.

This separation ensures decisions are based solely on the original configuration.

## Complexity Analysis

* **Time:** $O(mn)$ — every cell is inspected once in the scan and once in the write.
* **Space:** $O(m+n)$ — the two marker arrays.

## Source Code (Conceptual)

* **Pass 1:** build $R$ and $C$ by scanning for zeros.
* **Pass 2:** zero any $(i,j)$ with $i\in R$ or $j\in C$.

## Optional Optimization (O(1) Extra Space)

Use the first row and first column of `matrix` itself as the marker arrays:

* First, record two booleans: whether the original first row or first column contained a zero.
* Mark zeros by setting `matrix[i][0]=0` and `matrix[0][j]=0`.
* In a second pass (excluding row 0/col 0), zero cells based on those markers.
* Finally, zero the first row/column if their booleans were set.

This keeps time $O(mn)$ and reduces extra space to $O(1)$.
