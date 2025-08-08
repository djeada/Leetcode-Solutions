class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        marked_rows = [False] * m
        marked_cols = [False] * n

        # first pass, marking with no modyfications to the input matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    marked_rows[i] = True
                    marked_cols[j] = True


        # second, modyfication
        for i in range(m):
            for j in range(n):
                if marked_rows[i] or marked_cols[j]:
                    matrix[i][j] = 0

        
