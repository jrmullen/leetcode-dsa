class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        result = []
        parent = [i for i in range(n)] # The parent node
        size = [1] * n # The size of each component
        cost = [-1] * n # The minimum cost to walk each node
        
        # Find the root (parent) node of the provided `node`
        def find(node):
            # Traverse up the tree until a node whose parent is itself (the root node) is found
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Path compression
                node = parent[node]
            return node # Return the root node

        # Given 2 nodes `node1` & `node2`, combine their associated tree into 1 single tree
        def union(node1, node2):
            # Find the root node of each of the two nodes
            parent1 = find(node1)
            parent2 = find(node2)

            # If the parent node is the same, the nodes are already the part of the same tree. No action necessary
            if parent1 == parent2:
                return

            # Combine the two trees
            # The root node of the smaller tree becomes a child of the other tree's root node
            if size[parent1] < size[parent2]:
                parent[parent1] = parent2
                size[parent2] += size[parent1]
            else:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            return

        # First, build the graph by connecting all components
        for u, v, _ in edges:
            union(u, v)
        
        # Next, calculate the cost of each component
        for u, _, weight in edges:
            root = find(u)
            cost[root] &= weight

        # Finally, process each query
        for start, end in query:
            # If the vertexes are not in the same component, the walk is not possible
            root1 = find(start)
            root2 = find(end)
            if root1 != root2:
                result.append(-1)
            else:
                result.append(cost[root1])

        return result
