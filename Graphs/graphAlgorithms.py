import heapq
class Algorithms:
    def bfs(graph, start):
        visited = set()
        q = deque()
        q.add(start)
        while q:
            node = q.popleft()
            for neighbor in node.neighbors():
                q.add(neighbor)

    def dfs(graph, node, visited=None): # recursive dfs
        if visited = None:
            visited = set()
        if node not in visited:
            visited.add(node)
            for neighbor in node.neighbors:
                dfs(graph, neighbor, visited)

    def dijkstras(graph, start):
        # intitialize distances and priority queue
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)] # distance, node
        
        while pq:
            current_dist, current_node = heapq.heappop(pq)
            # skip if we already found a better path
            if current_dist > distances[current_node]:
                continue
            # explore neighbors 
            for neighbor, weight in graph[current_node]:
                distance = current_dist + weight
                # if shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance,neighbor))

        return distances
    
    def prim(graph, start):
        mst = [] # list to store MST edges: (weight, u, v)
        visited = set()
        min_heap = [(0, start, None)] # weight, current_node, from_node)
        
        while min_heap:
            weight, current, from_node = heapq.heappop(min_heap)

            if current in visited:
                continue
            visited.add(current)

            if from_node is not None:
                mst.append((from_node, current, weight))

            for neighbor, edge_weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush
                


