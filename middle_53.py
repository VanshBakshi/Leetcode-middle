class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # Word found
            if index == len(word):
                return True

            # Out of bounds or wrong character
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[index]:
                return False

            # Mark cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Search in 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Restore cell
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
