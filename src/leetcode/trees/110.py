# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root):
            if not root:
                return 0

            nonlocal balanced
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            # If the difference in height is more than 1, the tree is not balanced
            if abs(leftHeight - rightHeight) > 1:
                balanced = False

            return 1 + max(leftHeight, rightHeight)

        dfs(root)
        return balanced
