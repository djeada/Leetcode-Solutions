from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return
        
        m, n = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(start_corrdinates):
            reachable = [[False] * n for _ in range(m)]
            queue = deque(start_corrdinates)
            for row, col in start_corrdinates:
                reachable[row][col] = True

            while queue:
                row, col = queue.popleft()
                height = heights[row][col]
                for dir_row, dir_col in dirs:
                    ngh_row, ngh_col = row + dir_row, col + dir_col
                    if (
                        0 <= ngh_row < m and
                        0 <= ngh_col < n and
                        not reachable[ngh_row][ngh_col] and
                        height <= heights[ngh_row][ngh_col]
                    ):
                        reachable[ngh_row][ngh_col] = True
                        queue.append((ngh_row, ngh_col))

            return reachable

        pacific_starts = [(0, c) for c in range(n)] + [
            (r, 0) for r in range(m)
        ]
        atlantic_starts = [(m-1, c) for c in range(n)] + [
            (r, n-1) for r in range(m)
        ]

        pacific_result = bfs(pacific_starts)
        atlantic_result = bfs(atlantic_starts)

        return [
            (row, col) for row in range(m) for col in range(n)
            if pacific_result[row][col] and atlantic_result[row][col] 
        ]
