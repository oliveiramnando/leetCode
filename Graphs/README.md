# Graph Notes

## Graph Algorithms

*BFS for a Matrix with a queue*

```python
# Assume some matrix named grid, with r rows and c cols, where grid[r][c] == 1 has some significance
visited = set()
def bfs(r,c):
    visited.add((r,c))
    q = deque()
    q.append((r,c))

    while q:
        row, col = q.popleft()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for dr, dc in directions:
            r, c = row + dr, c + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1 and (r,c) not in visited:
                q.append((r,c))
                visited.add((r,c))
```

