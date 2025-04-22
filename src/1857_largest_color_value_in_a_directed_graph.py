class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        num_nodes = len(colors)
        # Build adjacency list
        graph = [[] for _ in range(num_nodes)]
        # Compute in-degrees for Kahn’s algorithm
        in_degree = [0] * num_nodes
        for src, dst in edges:
            graph[src].append(dst)
            in_degree[dst] += 1

        # dp_counts[node][c] = maximum number of occurrences of color c along
        # any path that ends at 'node'
        # We'll store this as a list of length 26 for each node
        dp_counts = [ [0]*26 for _ in range(num_nodes) ]

        # Initialize queue with all zero in-degree nodes
        topo_queue = deque()
        for node in range(num_nodes):
            if in_degree[node] == 0:
                topo_queue.append(node)

        processed_count = 0
        max_color_value = 0

        while topo_queue:
            node = topo_queue.popleft()
            processed_count += 1

            # Determine this node's character index (0 for 'a', 1 for 'b', etc.)
            char_idx = ord(colors[node]) - ord('a')
            # Count this node's own color on top of inherited counts
            dp_counts[node][char_idx] += 1

            # Update global maximum color value seen so far
            max_color_value = max(max_color_value, dp_counts[node][char_idx])

            # Propagate counts to neighbors
            for neighbor in graph[node]:
                # For each possible color c, see if going through 'node'
                # gives a better count at 'neighbor'
                for c in range(26):
                    if dp_counts[node][c] > dp_counts[neighbor][c]:
                        dp_counts[neighbor][c] = dp_counts[node][c]

                # Decrement in-degree and enqueue if it becomes zero
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    topo_queue.append(neighbor)

        # If we couldn't process all nodes, there's a cycle
        if processed_count < num_nodes:
            return -1

        return max_color_value
