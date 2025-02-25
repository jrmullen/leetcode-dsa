class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        def dfs_bob(node, time):
            bobTimes[node] = time
            visited.add(node)

            # Base case: the root node has been reached
            if node == 0:
                return True
            
            # DFS up the tree to the root node `0`
            for neighbor in adj[node]:
                if neighbor not in visited:
                    if dfs_bob(neighbor, time + 1):
                        return True
            
            del bobTimes[node]


        # DFS from node 0 to every leaf node, calculating the `total` at each move
        def dfs_alice(node, time, total):
            nonlocal result

            # Mark the current node as visited
            print(f'Visited node {node}')
            visited.add(node)

            # If the node is unvisited or was visited by Bob at a later point in time, add the `amount` to the `total`
            if node not in bobTimes or bobTimes[node] > time:
                total += amount[node]
            elif bobTimes[node] == time:
                total += amount[node] // 2

            # Base case: a leaf node (node with no children) has been reached
            if len(adj[node]) == 1 and node != 0:
                result = max(result, total)

            # DFS visiting every neighboring node
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs_alice(neighbor, time + 1, total)
        

        result = float('-inf') # Default to -inf so `max()` is reliable
        bobTimes = defaultdict(int) # Mapping {node: time unit the gate was opened}
        visited = set() # Avoid revisiting nodes while DFSing

        # First, build an adjacency list of the tree from the provided `edges`
        adj = defaultdict(list)
        for source, dest in edges:
            adj[source].append(dest)
            adj[dest].append(source)

        # DFS Bob first to populate the `bobTimes` dictionary with his moves
        dfs_bob(bob, 1)

        visited = set() # Reset the `visited` set for Alice

        # Finally, DFS Alice to calculate the best path
        dfs_alice(0, 1, 0)

        return result
