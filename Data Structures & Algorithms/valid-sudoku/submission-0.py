class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track numbers we've already encountered
        # We need 9 sets for rows, 9 for columns, and 9 for 3x3 squares
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                cell_value = board[r][c]

                # Skip empty cells
                if cell_value == ".":
                    continue
                
                # Determine which 3x3 square we are in (index 0-8)
                # This formula maps the 9x9 grid into nine 3x3 blocks
                square_index = (r // 3) * 3 + (c // 3)

                # Check if the value already exists in the current row, column, or square
                if (cell_value in rows[r] or 
                    cell_value in cols[c] or 
                    cell_value in squares[square_index]):
                    return False

                # Add the value to our trackers
                rows[r].add(cell_value)
                cols[c].add(cell_value)
                squares[square_index].add(cell_value)

        return True