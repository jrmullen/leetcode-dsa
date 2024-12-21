# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:     
        def dfs(leftNode, rightNode, level):
            # Base case: if there is not a left or right node the bottom of the tree has been reached
            if not leftNode or not rightNode:
                return

            # if the current level is odd, perform a swap on the node's values
            if level % 2 == 0:
                leftNode.val, rightNode.val = rightNode.val, leftNode.val

            # To reverse the order of a level:
            # swap the left child of the `leftNode` with the right child of the `rightNode`
            # swap the right child of the `leftNode` with the left child of the `rightNode`
            dfs(leftNode.left, rightNode.right, level + 1)
            dfs(leftNode.right, rightNode.left, level + 1)
        
        # Begin the DFS at the root node
        dfs(root.left, root.right, 0)
        return root
