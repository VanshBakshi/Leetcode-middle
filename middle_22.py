class Solution:
    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                # Ignore empty cells
                if value == ".":
                    continue

                # Find which 3x3 box this cell belongs to
                box = (r // 3) * 3 + (c // 3)

                # Check duplicate
                if value in rows[r]:
                    return False

                if value in cols[c]:
                    return False

                if value in boxes[box]:
                    return False

                # Add value
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True
