class Solution:
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]

        result = []

        for i in range(numRows):
            tmp = [0]* (i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    tmp[j] = 1
                else:
                    if i > 1:
                        tmp[j] = result[i-1][j-1] + result[i-1][j]
            result.append(tmp)

        return result