class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1   # closed interval [lo, hi]

        while lo <= hi:
            mid = (lo + hi) // 2
            x = matrix[mid // n][mid % n]  # map 1D index -> 2D (row, col)

            if x == target:
                return True
            elif x < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
