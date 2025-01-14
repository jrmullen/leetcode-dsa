class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list) # node: []

        # Construct an adjacency list to build the graph
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))

        # Prim's algorithm to find the Minimum Spanning Tree, tracking the total of each weighted edge
        result = 0
        heap = [(0, 0)] # (distance, node)
        visited = set()

        # Continue to DFS until all nodes have been connected
        while len(visited) < n:
            distance, node = heapq.heappop(heap)

            # Do not re-visit previously visited nodes
            if node in visited:
                continue
            
            # Include the `distance` to the node in the `result` counter
            result += distance

            # Mark the node as visited
            visited.add(node)
            
            # Add each neighboring node to the heap
            for neighborDistance, neighborNode in adj[node]:
                if neighborNode not in visited:
                    heapq.heappush(heap, (neighborDistance, neighborNode))
        
        return result
