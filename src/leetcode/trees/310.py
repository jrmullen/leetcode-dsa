class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        q = deque() # Queue to use for BFS

        # Base case: if there are 2 or less nodes
        if n <= 2:
            return [i for i in range(n)]

        # Build an adjacency list of the graph
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        # Identify the first leaf nodes and push them onto the queue to begin a BFS
        for i in range(n):
            if len(adj[i]) == 1:
                q.appendleft(i)
        
        # Trim leaf nodes via BFS until only the 2 centroid nodes are remaining
        while n > 2:
            num_leaves = len(q)
            n -= num_leaves

            # Remove the current batch of leaves along with their edges
            for _ in range(num_leaves):
                leaf = q.pop() # Pop the leaf node from the queue

                # Disconnect all neighboring nodes
                for neighbor in adj[leaf]:
                    adj[neighbor].remove(leaf) # Remove the neighboring node's connection
                    # If the neighboring node is the last remaining leaf node, push it onto the queue
                    if len(adj[neighbor]) == 1:
                        q.appendleft(neighbor)
        
        # The queue should contain the final 2 centroid nodes. Convert to a list and return
        return list(q)
