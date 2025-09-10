## Overview of the tags

| Problem | Primary Topic | All Tags |
|---|---|---|
| 3Sum | Array | Array, Two Pointers, Sorting |
| Best Time to Buy and Sell Stock | Array | Array, Sliding Window, Greedy |
| Container With Most Water | Array | Array, Two Pointers, Greedy |
| Contains Duplicate | Array | Array, Hash Set, Sorting |
| Find Minimum in Rotated Sorted Array | Array | Array, Binary Search |
| Maximum Product Subarray | Array | Array, Dynamic Programming |
| Maximum Subarray | Array | Array, Dynamic Programming, Kadane's Algorithm |
| Product of Array Except Self | Array | Array, Prefix Product |
| Search in Rotated Sorted Array | Array | Array, Binary Search |
| Two Sum | Array | Array, Hash Table |
| Counting Bits | Binary | Bit Manipulation, Dynamic Programming |
| Missing Number | Binary | Array, Bit Manipulation, Math |
| Number of 1 Bits | Binary | Bit Manipulation |
| Reverse Bits | Binary | Bit Manipulation |
| Sum of Two Integers | Binary | Bit Manipulation, Math |
| Climbing Stairs | Dynamic Programming | Dynamic Programming |
| Coin Change | Dynamic Programming | Dynamic Programming |
| Combination Sum | Dynamic Programming | Backtracking, DFS |
| Decode Ways | Dynamic Programming | Dynamic Programming, String |
| House Robber | Dynamic Programming | Dynamic Programming |
| House Robber II | Dynamic Programming | Dynamic Programming, Circular Array |
| Jump Game | Dynamic Programming | Greedy, Array, Dynamic Programming |
| Longest Common Subsequence | Dynamic Programming | Dynamic Programming, String |
| Longest Increasing Subsequence | Dynamic Programming | Dynamic Programming, Binary Search |
| Unique Paths | Dynamic Programming | Dynamic Programming, Combinatorics |
| Alien Dictionary (Leetcode Premium) | Graph | Graph, Topological Sort |
| Clone Graph | Graph | Graph, DFS, BFS, Hash Map |
| Course Schedule | Graph | Graph, Topological Sort, DFS, BFS |
| Graph Valid Tree (Leetcode Premium) | Graph | Graph, Union Find, DFS, BFS |
| Longest Consecutive Sequence | Graph | Hash Set, Array, Union Find |
| Number of Connected Components in an Undirected Graph (Leetcode Premium) | Graph | Graph, Union Find, DFS, BFS |
| Number of Islands | Graph | Matrix, Graph, DFS, BFS, Union Find |
| Pacific Atlantic Water Flow | Graph | Matrix, Graph, DFS, BFS |
| Insert Interval | Interval | Intervals, Greedy |
| Meeting Rooms (Leetcode Premium) | Interval | Intervals, Sorting |
| Meeting Rooms II (Leetcode Premium) | Interval | Intervals, Heap, Sweep Line |
| Merge Intervals | Interval | Intervals, Sorting |
| Non-overlapping Intervals | Interval | Intervals, Greedy, Sorting |
| Detect Cycle in a Linked List | Linked List | Linked List, Two Pointers |
| Merge K Sorted Lists | Linked List | Linked List, Heap, Divide and Conquer |
| Merge Two Sorted Lists | Linked List | Linked List, Divide and Conquer |
| Remove Nth Node From End Of List | Linked List | Linked List, Two Pointers |
| Reorder List | Linked List | Linked List, Two Pointers, Stack |
| Reverse a Linked List | Linked List | Linked List |
| Rotate Image | Matrix | Matrix, In-place, Simulation |
| Set Matrix Zeroes | Matrix | Matrix, Array |
| Spiral Matrix | Matrix | Matrix, Simulation |
| Word Search | Matrix | Backtracking, Matrix, DFS |
| Encode and Decode Strings (Leetcode Premium) | String | String, Design |
| Group Anagrams | String | String, Hash Map, Sorting |
| Longest Palindromic Substring | String | String, Dynamic Programming, Expand Around Center |
| Longest Repeating Character Replacement | String | String, Sliding Window, Hash Map |
| Longest Substring Without Repeating Characters | String | String, Sliding Window, Hash Map |
| Minimum Window Substring | String | String, Sliding Window, Hash Map |
| Palindromic Substrings | String | String, Dynamic Programming, Expand Around Center |
| Valid Anagram | String | String, Hash Map, Sorting |
| Valid Palindrome | String | String, Two Pointers |
| Valid Parentheses | String | Stack, String |
| Add and Search Word | Tree | Trie, Design, Backtracking |
| Binary Tree Level Order Traversal | Tree | Tree, BFS, Queue |
| Binary Tree Maximum Path Sum | Tree | Tree, DFS |
| Construct Binary Tree from Preorder and Inorder Traversal | Tree | Tree, Divide and Conquer, DFS |
| Implement Trie (Prefix Tree) | Tree | Trie, Design |
| Invert/Flip Binary Tree | Tree | Tree, DFS, BFS |
| Kth Smallest Element in a BST | Tree | Tree, BST, Inorder, Stack |
| Lowest Common Ancestor of BST | Tree | Tree, BST |
| Maximum Depth of Binary Tree | Tree | Tree, DFS, BFS |
| Same Tree | Tree | Tree, DFS, BFS |
| Serialize and Deserialize Binary Tree | Tree | Tree, Design, DFS, BFS |
| Subtree of Another Tree | Tree | Tree, DFS |
| Validate Binary Search Tree | Tree | Tree, BST, DFS, Inorder |
| Word Search II | Tree | Trie, Backtracking, DFS, Matrix |
| Find Median from Data Stream | Heap | Heap, Design, Two Heaps |
| Top K Frequent Elements | Heap | Heap, Hash Map, Bucket Sort |

## All Problems with short summaries

## Arrays (10)

* **Two Sum** *(LC 1)* — Use a hash map to store complements while scanning once; check if needed pair is already seen. *Time:* $O(n)$, *Space:* $O(n)$.
* **Best Time to Buy and Sell Stock** *(LC 121)* — Track the running minimum price and update max profit by comparing current price − min. *Time:* $O(n)$, *Space:* $O(1)$.
* **Contains Duplicate** *(LC 217)* — Insert elements into a set while scanning; if already present, duplicate found. Alternatively, sort then check neighbors. *Time:* $O(n)$ with set / $O(n \log n)$ with sort, *Space:* $O(n)$ or $O(1)$.
* **Product of Array Except Self** *(LC 238)* — Build prefix products left→right and suffix products right→left; multiply them for result. No division needed. *Time:* $O(n)$, *Space:* $O(1)$ extra (excluding output).
* **Maximum Subarray** *(LC 53)* — Kadane’s algorithm: keep running sum that resets if negative, track global max. *Time:* $O(n)$, *Space:* $O(1)$.
* **Maximum Product Subarray** *(LC 152)* — Track both current max and min products since negatives can flip signs; update global max. *Time:* $O(n)$, *Space:* $O(1)$.
* **Find Minimum in Rotated Sorted Array** *(LC 153)* — Binary search on pivot side; the min is the only element smaller than its left neighbor. *Time:* $O(\log n)$, *Space:* $O(1)$.
* **Search in Rotated Sorted Array** *(LC 33)* — Modified binary search: at each step decide which half is sorted and search only within it. *Time:* $O(\log n)$, *Space:* $O(1)$.
* **3Sum** *(LC 15)* — Sort array, then fix one index and use two pointers to find complementary pairs while skipping duplicates. *Time:* $O(n^2)$, *Space:* $O(1)$ (excluding output).
* **Container With Most Water** *(LC 11)* — Two-pointer technique: compute area, then move inward from the shorter wall since taller one cannot increase area. *Time:* $O(n)$, *Space:* $O(1)$.

### Bitwise (5)

* **Sum of Two Integers** *(LC 371)* — Use bitwise operators: XOR handles sum without carry, AND & shift computes carry; repeat until no carry remains. *Time:* $O(1)$ (bounded by 32 iterations), *Space:* $O(1)$.
* **Number of 1 Bits** *(LC 191)* — Repeatedly clear the lowest set bit with $n \wedge= (n-1)$ and count how many times until $n=0$. *Time:* $O(k)$, where $k$ = number of 1 bits, worst case $O(32)$, *Space:* $O(1)$.
* **Counting Bits** *(LC 338)* — DP relation: $\text{bits}[i] = \text{bits}[i \gg 1] + (i \wedge 1)$ (drop last bit + parity). Build array bottom-up. *Time:* $O(n)$, *Space:* $O(n)$.
* **Missing Number** *(LC 268)* — XOR all indices with all numbers; pairwise cancel leaves the missing value. Alternatively, subtract Gauss sum from actual sum. *Time:* $O(n)$, *Space:* $O(1)$.
* **Reverse Bits** *(LC 190)* — Initialize result = 0; for 32 steps, shift result left and append last bit of n, then shift n right. *Time:* $O(1)$ (32 iterations), *Space:* $O(1)$.

### Dynamic Programming (11)

* **Climbing Stairs** *(LC 70)* — Classic Fibonacci DP: number of ways to step $i$ is sum of previous two steps; only two variables needed. *Time:* $O(n)$, *Space:* $O(1)$.
* **Coin Change** *(LC 322)* — Bottom-up DP for unbounded knapsack: $\text{dp}[a] = \min(\text{dp}[a], \text{dp}[a-\text{coin}] + 1)$ for each amount. *Time:* $O(n \cdot m)$, with $n = \text{amount}, m = \text{coins}$, *Space:* $O(n)$.
* **Longest Increasing Subsequence** *(LC 300)* — Maintain an array of LIS tails; use binary search to place each number. Length of tails = LIS length. *Time:* $O(n \log n)$, *Space:* $O(n)$.
* **Longest Common Subsequence** *(LC 1143)* — 2D DP table comparing chars of both strings; optimize with rolling 1D row. *Time:* $O(m \cdot n)$, *Space:* $O(\min(m, n))$.
* **Word Break** *(LC 139)* — DP over prefixes: $\text{dp}[i] = \text{true}$ if any valid word ends at $i$ and prefix is breakable; dictionary membership checked each step. *Time:* $O(n^2)$ worst case, *Space:* $O(n)$.
* **Combination Sum** *(LC 39)* — Backtracking: recursively choose candidates in non-decreasing order, prune when sum > target. *Time:* Exponential in target/candidates, *Space:* $O(\text{target})$ recursion depth.
* **House Robber** *(LC 198)* — DP with two states: rob current + skip prev, or skip current. Rolling variables for $O(1)$ space. *Time:* $O(n)$, *Space:* $O(1)$.
* **House Robber II** *(LC 213)* — Because houses are circular, run House Robber on $[0..n-2]$ and $[1..n-1]$, return max. *Time:* $O(n)$, *Space:* $O(1)$.
* **Decode Ways** *(LC 91)* — DP over string indices: each digit (1–9) adds ways, and valid 2-digit numbers (10–26) add ways too; handle ‘0’ carefully. *Time:* $O(n)$, *Space:* $O(1)$ with rolling vars.
* **Unique Paths** *(LC 62)* — Grid DP where each cell = sum of top + left; or use combinatorial formula $\binom{m+n-2}{m-1}$. *Time:* $O(m \cdot n)$ for DP / $O(1)$ for combinatorics, *Space:* $O(\min(m, n))$.
* **Jump Game** *(LC 55)* — Greedy: track furthest index reachable so far; if current index > reach, fail. *Time:* $O(n)$, *Space:* $O(1)$.

### Graph (8)

* **Clone Graph** *(LC 133)* — Traverse with DFS or BFS, and for each node, create a clone stored in a hash map `old → new`. Recursively/iteratively link neighbors. *Time:* $O(V + E)$, *Space:* $O(V)$.
* **Course Schedule** *(LC 207)* — Detect cycles in a directed graph: either use Kahn’s topological sort (remove nodes with indegree 0) or DFS with recursion stack. *Time:* $O(V + E)$, *Space:* $O(V + E)$.
* **Pacific Atlantic Water Flow** *(LC 417)* — Instead of simulating each cell’s flow, run DFS/BFS *from the oceans inward*, marking reachable cells. Intersection gives valid coordinates. *Time:* $O(m \cdot n)$, *Space:* $O(m \cdot n)$.
* **Number of Islands** *(LC 200)* — Treat grid as graph; run DFS/BFS flood fill on each unvisited land cell, marking its whole island. Alternatively, Union-Find. *Time:* $O(m \cdot n)$, *Space:* $O(m \cdot n)$ (DFS stack/queue).
* **Longest Consecutive Sequence** *(LC 128)* — Store all numbers in a hash set. Only expand sequences from numbers that are sequence starts (no $x-1$). Count length of run. *Time:* $O(n)$, *Space:* $O(n)$.
* **Alien Dictionary** *(LC 269, Premium)* — Build a precedence graph by comparing adjacent words, adding edges for first differing chars. Then topologically sort with cycle detection. *Time:* $O(V + E)$, *Space:* $O(V + E)$.
* **Graph Valid Tree** *(LC 261, Premium)* — Use Union-Find to detect cycles and ensure all nodes are connected. For a tree: exactly $n-1$ edges and no cycles. *Time:* $O(E \cdot \alpha(V))$, *Space:* $O(V)$.
* **Connected Components in Undirected Graph** *(LC 323, Premium)* — Count components by DFS/BFS traversals or by Union-Find. Each traversal/union marks one component. *Time:* $O(V + E)$, *Space:* $O(V)$.

### Intervals (5)

* **Insert Interval** *(LC 57)* — Traverse intervals: add all non-overlapping before new interval, then merge overlaps into new interval, finally append the rest. *Time:* $O(n)$, *Space:* $O(1)$ extra.
* **Merge Intervals** *(LC 56)* — Sort by start time, then fold intervals into result: if current overlaps last merged, extend end; otherwise append new interval. *Time:* $O(n \log n)$, *Space:* $O(n)$ for output.
* **Non-overlapping Intervals** *(LC 435)* — Greedy: sort by end time, then keep intervals with earliest end; remove any that overlap. Count removals. *Time:* $O(n \log n)$, *Space:* $O(1)$.
* **Meeting Rooms** *(LC 252, Premium)* — Sort intervals by start time; check if any start < previous end. If so, overlap → not possible. *Time:* $O(n \log n)$, *Space:* $O(1)$.
* **Meeting Rooms II** *(LC 253, Premium)* — Track ongoing meetings: push end times into a min-heap; when a room frees, pop. Heap size = rooms needed. Sweep line alternative with sorted start/end arrays. *Time:* $O(n \log n)$, *Space:* $O(n)$.

### Linked List (6)

* **Reverse Linked List** *(LC 206)* — Iteratively reverse pointers: track `prev`, `curr`, `next`; at each step point `curr.next = prev`, then advance. *Time:* $O(n)$, *Space:* $O(1)$.
* **Linked List Cycle** *(LC 141)* — Use Floyd’s tortoise–hare: fast pointer moves $2\times$, slow moves $1\times$; if they meet, cycle exists. (Optional: reset one pointer to head to find entry.) *Time:* $O(n)$, *Space:* $O(1)$.
* **Merge Two Sorted Lists** *(LC 21)* — Use a dummy head; repeatedly append smaller node from the two lists until one is empty, then attach the remainder. *Time:* $O(m+n)$, *Space:* $O(1)$.
* **Merge K Sorted Lists** *(LC 23)* — Push list heads into a min-heap, repeatedly pop smallest and push its next. Alternative: divide & conquer merges. *Time:* $O(N \log k)$, where $N$ = total nodes, *Space:* $O(k)$.
* **Remove Nth Node From End** *(LC 19)* — Advance fast pointer $n$ steps ahead, then move slow + fast together until fast reaches end; delete `slow.next`. *Time:* $O(n)$, *Space:* $O(1)$.
* **Reorder List** *(LC 143)* — Split list at middle, reverse second half, then interleave nodes from first and reversed halves alternately. *Time:* $O(n)$, *Space:* $O(1)$.

### Matrix (4)

* **Set Matrix Zeroes** *(LC 73)* — Use first row and column as in-place markers for which rows/cols should be zeroed; track separately if first row/col should be zeroed. *Time:* $O(m \cdot n)$, *Space:* $O(1)$.
* **Spiral Matrix** *(LC 54)* — Maintain four boundaries (top, bottom, left, right); traverse in order ($\to, \downarrow, \leftarrow, \uparrow$), then shrink bounds inward until finished. *Time:* $O(m \cdot n)$, *Space:* $O(1)$.
* **Rotate Image** *(LC 48)* — For clockwise rotation: transpose matrix (swap across diagonal), then reverse each row. *Time:* $O(n^2)$, *Space:* $O(1)$.
* **Word Search** *(LC 79)* — Backtracking DFS: explore neighbors for each character, marking visited cells; backtrack to unmark. *Time:* $O(m \cdot n \cdot 4^L)$ worst case, $L = \text{word length}$, *Space:* $O(L)$ recursion depth.

### Strings (10)

* **Longest Substring Without Repeating Characters** *(LC 3)* — Sliding window with hash map from char $\to$ last index; shrink left when duplicate found. *Time:* $O(n)$, *Space:* $O(\min(n, \text{charset}))$.
* **Longest Repeating Character Replacement** *(LC 424)* — Sliding window; track frequency of chars and max freq in window. If $\text{window size} - \text{maxFreq} > k$, shrink left. *Time:* $O(n)$, *Space:* $O(26)$.
* **Minimum Window Substring** *(LC 76)* — Expand right pointer to satisfy all required chars, then contract left pointer to shrink window while valid. Maintain counts of “need” vs. “have.” *Time:* $O(n)$, *Space:* $O(|\text{charset}|)$.
* **Valid Anagram** *(LC 242)* — Count character frequencies in both strings and compare (or sort both and compare). *Time:* $O(n)$ with counts / $O(n \log n)$ with sort, *Space:* $O(1)$ (fixed alphabet).
* **Group Anagrams** *(LC 49)* — For each word, build key as sorted string or char-count tuple; group words by key in hash map. *Time:* $O(n \cdot k \log k)$ with sort, *Space:* $O(n \cdot k)$.
* **Valid Parentheses** *(LC 20)* — Use stack for open brackets; each close must match top of stack using a mapping. *Time:* $O(n)$, *Space:* $O(n)$.
* **Valid Palindrome** *(LC 125)* — Two pointers skipping non-alphanumeric chars; compare lowercase versions. *Time:* $O(n)$, *Space:* $O(1)$.
* **Longest Palindromic Substring** *(LC 5)* — Expand around each index as center (odd and even); track max length found. *Time:* $O(n^2)$, *Space:* $O(1)$.
* **Palindromic Substrings** *(LC 647)* — Similar to above, but count all palindromes during center expansions. *Time:* $O(n^2)$, *Space:* $O(1)$.
* **Encode and Decode Strings** *(LC 271, Premium)* — Encode with length-prefix format $\text{len}(\text{string})$ so delimiters don’t break decoding; parse sequentially. *Time:* $O(n)$, *Space:* $O(n)$.

### Trees / Trie (14)

* **Maximum Depth of Binary Tree** *(LC 104)* — DFS: return $1 + \max(\text{left}, \text{right})$ recursively; or BFS: count levels while traversing queue. *Time:* $O(n)$, *Space:* $O(h)$ for recursion or $O(n)$ for BFS.
* **Same Tree** *(LC 100)* — DFS recursively compare both structure and node values; must match in every subtree. *Time:* $O(n)$, *Space:* $O(h)$.
* **Invert/Flip Binary Tree** *(LC 226)* — Recursively swap left and right children at each node; can also do iteratively with queue/stack. *Time:* $O(n)$, *Space:* $O(h)$.
* **Binary Tree Maximum Path Sum** *(LC 124)* — DFS returns max downward path per node, while tracking global max including $\text{left} + \text{right} + \text{node}$. *Time:* $O(n)$, *Space:* $O(h)$.
* **Binary Tree Level Order Traversal** *(LC 102)* — BFS with a queue: push root, process nodes level by level into lists. *Time:* $O(n)$, *Space:* $O(n)$.
* **Serialize and Deserialize Binary Tree** *(LC 297)* — Use BFS with null markers (or preorder with `#` markers) to encode; deserialize by reconstructing. *Time:* $O(n)$, *Space:* $O(n)$.
* **Subtree of Another Tree** *(LC 572)* — For each node in main tree, check equality with subtree using DFS. Alternative: serialize trees and substring search (KMP). *Time:* $O(m \cdot n)$ worst / $O(m+n)$ with hashing, *Space:* $O(h)$.
* **Construct Binary Tree from Preorder & Inorder** *(LC 105)* — Use preorder to pick root; use hashmap of inorder indices to split left/right subtrees recursively. *Time:* $O(n)$, *Space:* $O(n)$.
* **Validate BST** *(LC 98)* — Recursive check with $(\min, \max)$ bounds at each node, or inorder traversal ensuring strictly increasing sequence. *Time:* $O(n)$, *Space:* $O(h)$.
* **Kth Smallest in BST** *(LC 230)* — Inorder traversal visits nodes in sorted order; stop at kth node. *Time:* $O(h + k)$, *Space:* $O(h)$.
* **Lowest Common Ancestor of BST** *(LC 235)* — Starting at root, move left or right depending on values; first split point is LCA. *Time:* $O(h)$, *Space:* $O(1)$.
* **Implement Trie (Prefix Tree)** *(LC 208)* — Each node holds map of children and `isEnd` flag; insert traverses chars, search/prefix checks path. *Time:* $O(L)$ per op, *Space:* $O(\text{total letters})$.
* **Add and Search Word** *(LC 211)* — Extend trie with DFS search to handle `.` wildcard by branching on all children. *Time:* $O(L \cdot \text{branches})$, *Space:* $O(\text{total letters})$.
* **Word Search II** *(LC 212)* — Build trie of words, then DFS board cells; prune when path not in trie and avoid revisiting cells. *Time:* $O(N \cdot 4^L)$ worst case (pruned by trie), *Space:* $O(\text{total letters} + \text{board})$.

### Heaps (2)

* **Top K Frequent Elements** *(LC 347)* — Count frequencies with a hash map. Then either:

  * **Bucket sort:** place numbers into buckets by frequency and collect from highest.
  * **Heap:** push $(\text{freq}, \text{num})$ into a min-heap of size $k$; pop when size exceeds $k$.
  * *Time:* $O(n)$ with bucket / $O(n \log k)$ with heap, *Space:* $O(n)$.
* **Find Median from Data Stream** *(LC 295)* — Maintain two heaps: max-heap for left half, min-heap for right half. Balance sizes so they differ by at most 1; median is top (or avg of tops). *Time:* $O(\log n)$ per insert, *Space:* $O(n)$.
