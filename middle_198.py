class Solution:
    def findWords(self, board, words):
        trie = {}

        # Build Trie
        for word in words:
            node = trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['$'] = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, parent):
            ch = board[r][c]

            if ch not in parent:
                return

            node = parent[ch]

            # Word found
            if '$' in node:
                result.append(node['$'])
                del node['$']

            # Mark cell as visited
            board[r][c] = '#'

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] != '#':
                        dfs(nr, nc, node)

            # Restore cell
            board[r][c] = ch

            # Remove exhausted Trie branches
            if not node:
                del parent[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result
