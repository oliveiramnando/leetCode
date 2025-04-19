class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        areaCount = [0]
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            area = 1
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r,c) not in visited:
                        area += 1
                        q.append((r,c))
                        visited.add((r,c))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    areaCount.append(bfs(r,c))

        return max(areaCount)

#---------- Alternative Method ----------#
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visited = set()
        max_island = 0
        
        def bfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or grid[r][c] == 0:
                return 0
            
            visited.add((r,c))

            return 1 + bfs(r + 1, c) + bfs(r - 1, c) + bfs(r, c + 1) + bfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    max_island = max(max_island, bfs(r,c))
        
        return max_island
