class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = rows * columns - 1

        while left <= right:
            mid = (left + right) // 2
            
            row = mid // columns
            column = mid % columns

            current = matrix[row][column]

            if current < target:
                left = mid + 1

            elif current > target:
                right = mid - 1
            else:
                return True
            
        return False