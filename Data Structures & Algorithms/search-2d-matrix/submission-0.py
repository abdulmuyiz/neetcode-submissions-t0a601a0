class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = (len(matrix) * len(matrix[0])) - 1
        while l <= h:
            mid = (h+l)// 2
            m = mid // len(matrix[0])
            n = mid % len(matrix[0])
            if matrix[m][n] == target:
                return True
            elif  matrix[m][n] < target:
                l = mid + 1
            elif  matrix[m][n] > target:
                h = mid - 1
        return False
