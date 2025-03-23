class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        parent = [i for i in range(n)]
        size = [1] * n
        edge_count = defaultdict(int)

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
            root1 = find(node1)
            root2 = find(node2)

            # If the two nodes share the same root they are already a part of the same component
            if root1 == root2:
                return
            
            # Combine the two trees
            # The root node of the smaller tree becomes a child of the other tree's root node
            if size[root1] >= size[root2]:
                parent[root2] = root1
                size[root1] += size[root2]
            else:
                parent[root1] = root2
                size[root2] += size[root1]
            return
        
        # Connect all edges to build each component
        for v1, v2 in edges:
            union(v1, v2)
        
        # Count the number of edges in each component
        for edge, _ in edges:
            root = find(edge)
            edge_count[root] += 1
        
        # Finally, count the number of complete components
        for vertex in range(n):
            # If the current vertex is a root node
            if find(vertex) == vertex:
                # For a component to be a complete component, each node in the component must have `k - 1` edges,
                # where `k` is the number of nodes in the component
                node_count = size[vertex]
                if edge_count[vertex] == (node_count * (node_count - 1)) // 2:
                    result += 1

        return result
