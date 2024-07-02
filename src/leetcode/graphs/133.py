"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeMap = {}

        def dfs(node):
            # Base case - if the current node is already in the `nodeMap`, return the cloned node
            if node in nodeMap:
                return nodeMap[node]

            clonedNode = Node(node.val, None)  # Create a clone of the current node containing no neighbors
            nodeMap[node] = clonedNode  # Add the clone node to the map of old->new nodes

            # DFS all of the neighbor nodes
            # The DFS returns a clone node, so use the returned node to populate the current node's neighbors
            for neighborNode in node.neighbors:
                clonedNode.neighbors.append(dfs(neighborNode))

            return clonedNode

        return dfs(node)
