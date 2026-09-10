class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        for row_index, row_value in enumerate(board):
            for col_index, col_value in enumerate(row_value):
                if col_value == ".":
                    continue

                box_num = (row_index // 3) * 3 + (col_index // 3)

                if (
                    col_value in row[row_index]
                    or col_value in col[col_index]
                    or col_value in box[box_num]
                ):
                    return False

                else:
                    row[row_index].add(col_value)
                    col[col_index].add(col_value)
                    box[box_num].add(col_value)

        return True
