from collections import deque
from typing import List, Tuple

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full_mask = self.compute_full_mask(n)
        visited = self.init_visited(n, full_mask)
        queue = self.init_queue(n, visited)

        return self.bfs_until_full_cover(graph, queue, visited, full_mask)

    @classmethod
    def compute_full_mask(cls, n: int) -> int:
        # e.g. for n=3, returns 0b111 == 7
        return (1 << n) - 1

    @classmethod
    def init_visited(cls, n: int, full_mask: int) -> List[List[bool]]:
        # visited[node][mask] = True if (node,mask) has been enqueued
        return [[False] * (full_mask + 1) for _ in range(n)]

    @classmethod
    def init_queue(
        cls,
        n: int,
        visited: List[List[bool]]
    ) -> deque[Tuple[int, int]]:
        q = deque()
        for node in range(n):
            mask = 1 << node
            q.append((node, mask))
            visited[node][mask] = True
        return q

    @classmethod
    def bfs_until_full_cover(
        cls,
        graph: List[List[int]],
        queue: deque[Tuple[int, int]],
        visited: List[List[bool]],
        full_mask: int
    ) -> int:
        steps = 0
        while queue:
            for _ in range(len(queue)):
                node, mask = queue.popleft()

                if mask == full_mask:
                    return steps

                for neighbour in graph[node]:
                    next_mask = mask | (1 << neighbour)
                    if not visited[neighbour][next_mask]:
                        visited[nei][next_mask] = True
                        queue.append((neighbour, next_mask))
            steps += 1

        return -1
        
