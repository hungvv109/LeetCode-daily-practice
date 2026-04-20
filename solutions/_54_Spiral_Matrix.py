class Solution:
    def spiralOrder(self, matrix):
        x = 0
        m = len(matrix)
        n = len(matrix[0])
        all_ele = m*n
        res = []
        check = 0

        while True:
            for j in range(x, n-x):
                res.append(matrix[x][j])
                check += 1

            if check == all_ele:
                break

            x += 1
            for i in range(x, m-x+1):
                res.append(matrix[i][n-x])
                check += 1

            if check == all_ele:
                break

            for j in range(n-1-x, x-2,-1):
                res.append(matrix[m-x][j])
                check += 1

            if check == all_ele:
                break

            for i in range(m-1-x, x-1,-1):
                res.append(matrix[i][x-1])
                check += 1

            if check == all_ele:
                break

        return res