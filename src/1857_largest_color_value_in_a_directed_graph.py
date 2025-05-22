from collections import deque
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """
        Return the maximum number of occurrences of any single color along any path
        in the directed graph defined by 'edges', or -1 if the graph has a cycle.
        """
        n = len(colors)
        adjacency = self._build_graph(n, edges)
        in_degree = self._compute_in_degrees(n, edges)

        # color_counts[node][c] = max occurrences of color c ('a'→0, …, 'z'→25)
        color_counts = [[0] * 26 for _ in range(n)]
        queue = deque(i for i in range(n) if in_degree[i] == 0)

        processed = 0
        max_value = 0

        while queue:
            node = queue.popleft()
            processed += 1

            # Count this node's own color
            idx = ord(colors[node]) - ord('a')
            color_counts[node][idx] += 1
            max_value = max(max_value, color_counts[node][idx])

            # Propagate counts to each neighbor
            for neigh in adjacency[node]:
                self._propagate(color_counts, node, neigh)
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    queue.append(neigh)

        # If not all nodes were processed, there's a cycle
        return max_value if processed == n else -1

    def _build_graph(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for src, dst in edges:
            graph[src].append(dst)
        return graph

    def _compute_in_degrees(self, n: int, edges: List[List[int]]) -> List[int]:
        in_deg = [0] * n
        for _, dst in edges:
            in_deg[dst] += 1
        return in_deg

    def _propagate(self, counts: List[List[int]], src: int, dst: int) -> None:
        """
        For each color c, update counts[dst][c] to be the max of its current value
        and counts[src][c], effectively propagating best-path counts forward.
        """
        for c in range(26):
            if counts[src][c] > counts[dst][c]:
                counts[dst][c] = counts[src][c]
