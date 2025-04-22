from typing import List

class Solution:
    def criticalConnections(self, server_count: int, connections: List[List[int]]) -> List[List[int]]:
        # 1) Build adjacency list
        adjacency_list = [[] for _ in range(server_count)]
        for u, v in connections:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)

        # 2) Prepare arrays for discovery time and low-link values
        discovery_time = [-1] * server_count
        low_link = [0] * server_count
        time_stamp = 0

        bridge_edges: List[List[int]] = []

        # 3) Iterative DFS stack entries: (node, parent, next_neighbor_index)
        dfs_stack: List[tuple[int, int, int]] = []

        # 4) Process each component
        for start_server in range(server_count):
            if discovery_time[start_server] != -1:
                continue

            # Begin DFS at start_server
            dfs_stack.append((start_server, -1, 0))

            while dfs_stack:
                node, parent, neighbor_idx = dfs_stack.pop()

                # First time we see this node
                if neighbor_idx == 0:
                    discovery_time[node] = time_stamp
                    low_link[node] = time_stamp
                    time_stamp += 1

                # Iterate over neighbors starting from neighbor_idx
                while neighbor_idx < len(adjacency_list[node]):
                    neighbor = adjacency_list[node][neighbor_idx]
                    neighbor_idx += 1

                    if discovery_time[neighbor] == -1:
                        # Tree edge: push current frame back with updated index,
                        # then push child frame to process neighbor
                        dfs_stack.append((node, parent, neighbor_idx))
                        dfs_stack.append((neighbor, node, 0))
                        break
                    elif neighbor != parent:
                        # Back edge: update low-link immediately
                        low_link[node] = min(low_link[node], discovery_time[neighbor])
                else:
                    # All neighbors processed: time to backtrack
                    if parent != -1:
                        # Update parent's low-link based on this node
                        low_link[parent] = min(low_link[parent], low_link[node])
                        # If no back-edge from node or its subtree reaches above parent,
                        # then (parent, node) is a bridge
                        if low_link[node] > discovery_time[parent]:
                            bridge_edges.append([parent, node])
                    # No need to push the frame back—this branch is done

        return bridge_edges
