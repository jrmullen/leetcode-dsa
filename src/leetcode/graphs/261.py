class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodeMap = { i:[] for i in range(n) }
        visited = set()

        # Populate `nodeMap` with all edges
        for a, b in edges:
            nodeMap[a].append(b)
            nodeMap[b].append(a)
        
        def dfs(node, previousNode):
            # Base case - a node previously visited node is encountered. There is a cycle in the graph, & therefore not a tree
            if node in visited:
                return False
            
            # Mark the current node as visited
            visited.add(node)

            # Visit all neighboring nodes
            for neighbor in nodeMap[node]:
                if neighbor == previousNode:
                    continue # Do not re-visit the last node node - continue down the tree
                if not dfs(neighbor, node):
                    return False # A cycle has been detected, and therefore the graph cannot be a valid tree

            return True
        
        # Start at node 0 with a dummy `previousNode` value
        result = dfs(0, -1) # If a cycle is detected `dfs()` will return `False` - it is not a tree
        allNodesVisited = len(visited) == n # If all nodes were not reachable from the root node, it is not a tree
        return result and allNodesVisited
