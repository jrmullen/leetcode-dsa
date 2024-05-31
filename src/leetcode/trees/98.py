# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left, right):
            if not node:
                return True

            # If the value of the node is not within the left and right bounds, it is not a valid BST
            if not (node.val < right and node.val > left):
                return False

            # Recursively compare the results of the left and right child nodes
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        # Perform a DFS initial bounds to -infinity < node.val < +infinity
        return dfs(root, float('-inf'), float('inf'))
