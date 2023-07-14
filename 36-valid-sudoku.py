class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check square, use row//3, col//3 as the square ID
        # This can not be reset during the whole check procedure
        check_set_for_square_map = collections.defaultdict(set)

        for i in range(9):
            # Chech each row, this need to be reset after one row iteration
            check_set_for_row = set()
            # Check each col, this need to be reset after one col iteration
            check_set_for_col = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in check_set_for_row: # check row
                    return False
                else:
                    check_set_for_row.add(board[i][j])
                if board[j][i] != "." and board[j][i] in check_set_for_col: # check col
                    return False
                else:
                    check_set_for_col.add(board[j][i])

                # Check square with suqare map ID = str(i//3)+str(j//3)
                if board[i][j] != "." and board[i][j] in check_set_for_square_map[str(i//3)+str(j//3)]:
                    return False
                else:
                    check_set_for_square_map[str(i//3)+str(j//3)].add(board[i][j])

        return True