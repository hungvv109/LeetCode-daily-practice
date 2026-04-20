class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for x in range(n):
            for y in range(x+1, n):
                matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

        for row in matrix:
            row.reverse()