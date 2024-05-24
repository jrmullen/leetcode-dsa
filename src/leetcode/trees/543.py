# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0
            
            # use `nonlocal` to reference the variable scoped outside of `dfs()`
            nonlocal longest
            leftHeight = dfs(root.left) # Depth first search to find the height of the left node
            rightHeight = dfs(root.right) # Depth first search to find the height of the right node

            # Depth = height of left node + height of right node
            longest = max(longest, leftHeight + rightHeight)

            # Return the height of the tree
            return 1 + max(leftHeight, rightHeight)
        
        dfs(root)
        return longest
