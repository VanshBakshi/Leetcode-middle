class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue

                num = board[r][c]

                # Check row
                if num in rows[r]:
                    return False
                rows[r].add(num)

                # Check column
                if num in cols[c]:
                    return False
                cols[c].add(num)

                # Find 3x3 box
                box = (r // 3) * 3 + (c // 3)

                if num in boxes[box]:
                    return False
                boxes[box].add(num)

        return True
