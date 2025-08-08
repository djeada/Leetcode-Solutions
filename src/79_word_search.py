class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, word_index):
            if word_index == len(word):
                return True

            if (i < 0 or i >= m or j < 0 or j >= n or word[word_index] != board[i][j]):
                return False

            tmp = board[i][j]
            board[i][j] = '#'

            found = (dfs(i + 1, j, word_index + 1) or dfs(i - 1, j, word_index + 1) or dfs(i, j + 1, word_index + 1) or dfs(i, j - 1, word_index + 1))

            board[i][j] = tmp
            
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
        
