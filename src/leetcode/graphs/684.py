class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        size = [1] * (len(edges) + 1)

        # Given a node `node`, return it's tree's root node
        def find(node):
            # The root note will be its own parent. Traverse up the tree until the root node is found
            while node != parent[node]:
                parent[node] = parent[parent[node]] # Path compression - return the grandparent if possible to flatten the tree
                node = parent[node]
            return node
        
        # Given 2 nodes `node1` & `node2`, combine their associated trees into 1 single tree
        def union(node1, node2):
            # Find the root of each node's tree
            parent1 = find(node1)
            parent2 = find(node2)

             # If the parent node is the same, the nodes are already the part of the same tree - redundant connection
            if parent1 == parent2:
                return [node1, node2]

            # Combine the two trees
            # The root node of the smaller tree becomes a child of the other tree's root node
            if size[parent2] > size[parent1]:
                parent[parent1] = parent2
                size[parent2] += size[parent1]
            else:
                parent[parent2] = parent1
                size[parent1] += size[parent2]
            return None
        
        for a, b in edges:
            redundantEdge = union(a, b)
            if redundantEdge:
                return redundantEdge
