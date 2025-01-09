class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list) # source: (dest, weight)
        heap = [(0, k)] # (weight, node) -- Pre-populate the starting node `k` with a weight of `0`
        visited = set()
        
        # Construct a weighted adjacency list
        for source, dest, weight in times:
            edges[source].append((dest, weight))
        
        # Track the total `time` that has elapsed
        time = 0
        while heap:
            # Pop the node with the smallest `weight` from the top of the `heap`
            weight, node = heapq.heappop(heap)

            if node in visited:
                continue

            # Mark the node as visited
            visited.add(node)

            # Update the `time` counter
            time = weight

            # Visit each unvisited neighbor node
            for neighbor, neighbor_weight in edges[node]:
                if neighbor not in visited:
                    # Push the `neighbor` node onto the heap with it's combined weight value `weight + neighbor_weight`
                    heapq.heappush(heap, (weight + neighbor_weight, neighbor))

        # If all nodes were successfully visited, return the total `time` taken
        return time if len(visited) == n else -1
