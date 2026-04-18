class Solution:
    def binary_search(self, grid, a, b):
        if a == b:
            if grid[a] > -1:
                return -1
            return 0

        while a < b:
            mid = (a + b) // 2
            if grid[mid] < 0:
                b = mid
            else:
                a = mid + 1

        if a == (len(grid)-1) and grid[a] > -1: 
            return -1
        return a

    def countNegatives(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        for i in range(m):
            idx = self.binary_search(grid[i], 0, n-1)
            if idx != -1:
                count += (n-idx)

        return count