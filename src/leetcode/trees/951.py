# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Base case: if one of the trees is empty they will never be equivalent
        if not root1 or not root2:
            # If both trees are empty return True, else False
            return not root1 and not root2
        
        # Base case: the root nodes have different values
        if root1.val != root2.val:
            return False
        
        # Recurse on the sub-trees
        notSwapped = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        swapped = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)

        return swapped or notSwapped
