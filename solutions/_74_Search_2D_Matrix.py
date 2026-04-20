class Solution:
    def binarySearch_row(self, matrix, target):
        left, right = 0, len(matrix) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result if matrix[result][0] != target else -10

    def binarySearch(self, matrix, target):
        left, right = 0, len(matrix) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid] <= target:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result if matrix[result] != target else -10


    def searchMatrix(self, matrix, target) -> bool:
        i_row = self.binarySearch_row(matrix, target)

        if i_row == -10:
            return True

        i_col = self.binarySearch(matrix[i_row], target)

        if i_col == -10:
            return True
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(Solution().searchMatrix(matrix, target))