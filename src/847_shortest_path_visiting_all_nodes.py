from collections import deque
from typing import List

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        node_count = len(graph)
        # A bitmask with node_count bits all set to 1 (e.g. for n=3, full_mask=0b111)
        full_mask = (1 << node_count) - 1

        # visited_states[node][mask] = True if we've visited the state (node, mask)
        visited_states = [ [False] * (1 << node_count) for _ in range(node_count) ]

        # Initialize BFS queue with each node as a starting point
        # Each entry is (current_node, visited_mask)
        bfs_queue = deque()
        for start_node in range(node_count):
            start_mask = 1 << start_node
            bfs_queue.append((start_node, start_mask))
            visited_states[start_node][start_mask] = True

        steps = 0
        # Standard BFS over the state graph
        while bfs_queue:
            for _ in range(len(bfs_queue)):
                current_node, visited_mask = bfs_queue.popleft()
                
                # If we've visited all nodes, return the number of steps taken
                if visited_mask == full_mask:
                    return steps

                # Try moving to each neighbor
                for neighbor in graph[current_node]:
                    next_mask = visited_mask | (1 << neighbor)
                    if not visited_states[neighbor][next_mask]:
                        visited_states[neighbor][next_mask] = True
                        bfs_queue.append((neighbor, next_mask))

            steps += 1

        # The graph is connected, so we should always return inside the loop
        return -1
