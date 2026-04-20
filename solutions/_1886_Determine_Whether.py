class Solution:
    def findRotation(self, mat, target) -> bool:
        n = len(mat)
        check = False

        if mat == target:
            return True

        for _ in range(3):
            for i in range(n):
                for  j in range(i+1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for row in mat:
                row.reverse()

            check = (mat == target)

            if check:
                return True
        return False

