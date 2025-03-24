class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        MOD = 10**9 + 7

        # First, build an adjacency list of the undirected graph
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        
        # Diejkstra's to find the shortest path to each node
        heap = [(0, 0)] # (time, node)
        min_time = [float('inf')] * n # Track the minimum time to get to each node
        path_count = [0] * n # Count the number of paths to a node
        path_count[0] = 1 # Default case: there is 1 way to get to the starting node `0`
        
        while heap:
            # Pop the nearest node off the heap
            time, node = heapq.heappop(heap)
            
            # Iterate over each neighboring node
            for neighbor, neighbor_time in adj[node]:
                # If a new shortest path is found, adjust the `min_time` and `path_count`
                if time + neighbor_time < min_time[neighbor]:
                    min_time[neighbor] = time + neighbor_time
                    path_count[neighbor] = path_count[node]
                    heapq.heappush(heap, (time + neighbor_time, neighbor)) # Push the neighboring node onto the heap
                elif time + neighbor_time == min_time[neighbor]: # If the times are the same, update the `path_count`
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD # Mod to keep the number of paths from growing too large

        # Return the number of shortest paths to the last node
        return path_count[n - 1]
