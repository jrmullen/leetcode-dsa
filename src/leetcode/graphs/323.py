class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        result = n

        # Given a node `node`, return its root node
        def find(node):
            # Traverse up the tree until a node that is its own parent (the root node) is found
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Path compression - return the grandparent if possible to flatten the tree
                node = parent[node]
            return node
        
        # Given 2 nodes `node1` & `node2`, combine their associated trees into 1 single tree
        def union(node1, node2):
            # Find the root of each node's tree
            parent1 = find(node1)
            parent2 = find(node2)

            # If the parent node is the same, the nodes are already the part of the same tree. No action necessary
            if parent1 == parent2:
                return 0
            
            # Combine the two trees
            # The root node of the smaller tree becomes a child of the other tree's root node
            if size[parent2] > size[parent1]:
                parent[parent1] = parent2
                size[parent2] += size[parent1]
            else:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            
            # Return `1` to signify that a parent was re-assigned
            return 1
        
        for a, b in edges:
            # `result` starts at size `n`
            # Every time a union is performed there is 1 less unconnected node
            result -= union(a, b)
        
        return result
