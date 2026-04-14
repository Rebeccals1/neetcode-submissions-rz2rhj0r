class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We track everything in one place: 
        # Keys will be tuples like ('row', 0), ('col', 5), or ('square', (0, 1))
        seen_elements = set()

        for r in range(9):
            for c in range(9):
                cell_value = board[r][c]

                # 1. Skip empty cells (The "Guard Clause")
                if cell_value == ".":
                    continue
                
                # 2. Define our unique coordinate tuples
                row_key = ("row", r, cell_value)
                col_key = ("col", c, cell_value)
                
                # The square is identified by its (block_row, block_col) coordinate
                square_coords = (r // 3, c // 3)
                square_key = ("square", square_coords, cell_value)

                # 3. Check if this specific number has been seen in these contexts
                if (row_key in seen_elements or 
                    col_key in seen_elements or 
                    square_key in seen_elements):
                    return False

                # 4. Mark these combinations as "seen"
                seen_elements.add(row_key)
                seen_elements.add(col_key)
                seen_elements.add(square_key)

        return True