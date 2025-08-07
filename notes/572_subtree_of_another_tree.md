## Data Structures

**Inputs:**

* `T`: binary tree with $N$ nodes (rooted at `root`).
* `S`: binary tree with $M$ nodes (rooted at `subRoot`).

**Auxiliary Variables:**

* `node`, `subNode`: pointers used by the helper `isSame` to walk two trees in tandem.

## What Happens in `isSubtree`?

We reduce the problem to two tasks:

1. **Tree‐Equality Check** (`isSame`): decide if two trees of sizes $m$ and $m$ are identical in structure and node‐values.
2. **Traversal**: scan every node of $T$, invoking the equality check at each one until we find a match or exhaust $T$.

```mermaid
flowchart TD
  A[Start at root of T] --> B{root is null?}
  B -->|Yes| C[Return False]
  B -->|No| D{isSame(root, subRoot)?}
  D -->|Yes| E[Return True]
  D -->|No| F[Recurse on left subtree]
  F --> G{left yields True?}
  G -->|Yes| E
  G -->|No| H[Recurse on right subtree]
  H --> I{right yields True?}
  I -->|Yes| E
  I -->|No| C
  C & E --> J[Done]
```

### I. Helper: `isSame(node, subNode)`

We perform a synchronized preorder traversal of the two trees:

1. **Both null**: return **True**.
2. **One null**: return **False**.
3. **Value mismatch**: return **False**.
4. **Otherwise**: recurse on left children **and** right children.

Mathematically, if we denote by

$$
  \mathrm{Same}(u,v)
$$

the predicate “subtrees at $u$ and $v$ are identical,” then

$$
  \mathrm{Same}(u,v)
  = 
  \begin{cases}
    \text{True}, & u=v=\mathrm{null},\\
    \text{False},& \text{exactly one is null or }u.\mathrm{val}\neq v.\mathrm{val},\\
    \mathrm{Same}(u.\mathrm{left},v.\mathrm{left}) 
     \;\wedge\;
     \mathrm{Same}(u.\mathrm{right},v.\mathrm{right}), & \text{otherwise.}
  \end{cases}
$$

### II. Main Procedure: `isSubtree(root, subRoot)`

We define

$$
  \mathrm{Sub}(u,S)
$$

as “tree at node $u$ contains $S$ as a subtree.” Then

$$
  \mathrm{Sub}(u,S)
  =
  \mathrm{Same}(u,S)
  \;\vee\;
  \mathrm{Sub}(u.\mathrm{left},S)
  \;\vee\;
  \mathrm{Sub}(u.\mathrm{right},S).
$$

At each node $u$ of $T$, we first test $\mathrm{Same}(u,S)$; if that fails, we recursively query the left and right children of $u$.

## Example

Let

$$
T = 
\begin{array}{c}
\;3\\
/\;\;\backslash\\
4\;\;\;5\\
/\;\backslash\\
1\;\;2
\end{array}
\quad
S=
\begin{array}{c}
4\\
/\;\backslash\\
1\;\;2
\end{array}
$$

* At $u=3$, $\mathrm{Same}(3,S)$ fails (values differ).
* Recurse to $u=4$: now $\mathrm{Same}(4,S)$ holds, since both structure and values match exactly.
  → return **True**.

## Complexity Analysis

* **Time Complexity:**
  In the worst case, for each of the $N$ nodes in $T$ we invoke `isSame`, which may explore up to $M$ nodes.

  $$
    O(N\times M).
  $$
* **Space Complexity:**
  Recursion depth is bounded by the height of $T$, say $H$, so

  $$
    O(H).
  $$
