class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        # Convert the `marked` list into a HashSet for efficient lookups
        marked = set(marked)

        # Create an adjacency list to build the directed, weighted graph
        adj = defaultdict(list)
        for source, dest, weight in edges:
            adj[source].append((dest, weight)) # Map source -> tuple (destination, weight)
        
        # Initialize a minHeap and push the starting node onto it with a distance of 0
        heap = [] # Tuple (distance, dest)
        heapq.heappush(heap, (0, s))

        # Initialize a map to track the distance to each node
        distances = defaultdict(int)
        distances[s] = 0 # Default the starting node `s` with a distance of 0

        # BFS Dijkstra's algorithm until a node in the `marked` set is visited
        while heap:
            distance, node = heapq.heappop(heap)

            # If the current `node` is one of the `marked` nodes, return the current `distance`
            if node in marked:
                return distance
            
            # Push each neighboring node onto the heap with its distance from the starting node
            for neighbor, weight in adj[node]:
                new_distance = distance + weight

                # Do not visit previously visited nodes unless a shorter distance has been calculated
                if neighbor not in distances or new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance # Update the distance in the `distances` map
                    heapq.heappush(heap, (new_distance, neighbor)) # Push the node onto the `heap`
        
        # Fionally, if a marked node was not able to be hit, return the default value
        return -1
