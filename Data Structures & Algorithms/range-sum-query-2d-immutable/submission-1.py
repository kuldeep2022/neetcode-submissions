class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        # prefix[r][c] stores the sum of the rectangle
        # from (0, 0) to (r - 1, c - 1)
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            row_sum = 0

            for c in range(cols):
                row_sum += matrix[r][c]

                # Sum above the current cell
                above = self.prefix[r][c + 1]

                self.prefix[r + 1][c + 1] = row_sum + above

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int
    ) -> int:
        # Shift coordinates because prefix has an extra row and column
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        bottom_right = self.prefix[row2][col2]
        above = self.prefix[row1 - 1][col2]
        left = self.prefix[row2][col1 - 1]
        top_left = self.prefix[row1 - 1][col1 - 1]

        # Inclusion-exclusion
        return bottom_right - above - left + top_left