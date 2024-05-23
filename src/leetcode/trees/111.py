# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        # Ignore 0
        if leftDepth == 0:
            return 1 + rightDepth
        elif rightDepth == 0:
            return 1 + leftDepth

        # Else take the small of the 2
        return 1 + min(leftDepth, rightDepth)
