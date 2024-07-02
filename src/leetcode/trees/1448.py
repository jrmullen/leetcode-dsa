# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        # DFS, including the largest node value encountered
        def dfs(node, largest):
            if not node:
                return

            nonlocal result
            # If the node value is larger than the largest node encountered so far, it is a good node
            if node.val >= largest:
                result += 1
            
            # Recalculate the max to account for the node that is being visited
            largest = max(largest, node.val)
            dfs(node.left, largest)
            dfs(node.right, largest)

        dfs(root, root.val)
        return result
