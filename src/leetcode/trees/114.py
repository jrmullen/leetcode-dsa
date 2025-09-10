# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Define a new function to flatten the tree in order to have a return value
        # Return the rightmost node
        def dfs(root):
            # Base case: the root node does not exist
            if not root:
                return None

            left_tail = dfs(root.left)
            right_tail = dfs(root.right)

            if left_tail:
                left_tail.right = root.right
                root.right = root.left
                root.left = None
            
            # Always return the rightmost node - the right_tail will have the rightmost node, but if it is empty
            # then the left_tail will have the rightmost node, but if it is empty then the root will have the rightmost node
            return right_tail if right_tail else left_tail if left_tail else root

        # DFS starting at the root            
        dfs(root)
