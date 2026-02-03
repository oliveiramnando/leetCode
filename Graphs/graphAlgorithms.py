import heapq
class Algorithms:

    #----------Traversal----------#
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

    #----------Shortest Path Algorithms----------#
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

        # Handling of unreachable node
        for node in distances:
            if distances[node] == float('inf'):
                distances[node] = -1

        return distances

    def dijkstrasVTwo(graph, n: int, edges: List[List[int]], src:int)->Dict[int, int]:
        adj = {i: [] for i in range(1, n + 1)}
        for s, d, w in times:
            adj[s].append((d, w))

        shortest = {}
        minHeap = [(0, k)] 

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in shortest:
                continue
            shortest[n1] = w1
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        if len(shortest) < n:
            return -1

        return shortest
    
    def bellman_ford(V, edges, src):
        # Initially distance from source to all other vertices 
        # is not known(Infinite) e.g. 1e8.
        dist = [100000000] * V
        dist[src] = 0

        # Relaxation of all the edges V times, not (V - 1) as we
        # need one additional relaxation to detect negative cycle
        for i in range(V):
            for edge in edges:
                u, v, wt = edge
                if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                    # If this is the Vth relaxation, then there 
                    # is a negative cycle
                    if i == V - 1:
                        return [-1]
                    # Update shortest distance to node v
                    dist[v] = dist[u] + wt
        return dist

    #----------Minimum Spanning Trees----------#   
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
                
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] self.find(self.parent[x])
            return self.parent[x]
        def union(self, x, y):
            xr = self.find(x)
            yr = self.find(y)
            if xr == yr:
                return False
            if self.rank[xr] < self.rank[yr]:
                self.parent[xr] = yr
            elif self.rank[xr] > self.rank[yr]:
                self.parent[yr] = xr
            else:
                self.parent[yr] = xr
                self.rank[xr] += 1
            return True
    
    def kruskal(n, edges):
        """
        :param n: number of vertices
        :param edges:  List of edges [u,v,weight]
        :return: Total weight of the MST



