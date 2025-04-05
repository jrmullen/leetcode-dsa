# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # Recursively search for the LCA of the current `node`'s left and right subtrees
        def dfs(node, depth):
            # Base case: the current `node` is empty
            if not node:
                return (None, depth + 1) # LCA, depth
            
            lca_left, depth_left = dfs(node.left, depth + 1)
            lca_right, depth_right = dfs(node.right, depth + 1)

            if depth_left > depth_right: # If the height of the left subtree is larger, the LCA will be the left subtree's LCA
                return (lca_left, depth_left)
            elif depth_right > depth_left: # If the height of the right subtree is larger, the LCA will be the right subtree's LCA
                return (lca_right, depth_right)
            # If both left and right subtrees are of the same height, the current node is the LCA
            return (node, depth_left)
        
        # DFS to find the LCA starting at the `root` node with a depth of 0
        return dfs(root, 0)[0] # Return the first return value of the tuple (lca, depth)
