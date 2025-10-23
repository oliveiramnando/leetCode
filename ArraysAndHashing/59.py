class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res =[[i for i in range(n)] for i in range(n)]

        rows, cols = len(res), len(res[0])
        top, bottom, left, right = 0, rows-1, 0, cols-1

        counter = []
        ticker = 1
        while len(counter) < rows * cols:
            for i in range(left, right+1):
                counter.append(res[top][i])
                res[top][i] = ticker
                ticker += 1

            top += 1
            
            for i in range(top, bottom+1):
                counter.append(res[i][right])
                res[i][right] = ticker
                ticker += 1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    counter.append(res[bottom][i])
                    res[bottom][i] = ticker
                    ticker += 1
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    counter.append(res[i][left])
                    res[i][left] = ticker
                    ticker += 1
                left += 1
        
        return res
