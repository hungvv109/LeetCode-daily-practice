class Solution:
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        if m*n != r*c:
            return mat

        res = []
        check = 0
        tmp = []

        for i in range(m):
            for j in range(n):
                tmp.append(mat[i][j])
                check += 1
                if check == c:
                    res.append(tmp)
                    tmp = []
                    check = 0
        return res

mat = [[1,2],[3,4]]
r = 1
c = 4
print(Solution().matrixReshape(mat, r, c))