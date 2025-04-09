# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Inorder Traversal: left, root, right
        def dfs(node):
            # Base case: the current `node` is empty
            if not node:
                return

            # Traverse the left subtree
            if node.left:
                dfs(node.left)
            
            # Append the current node's value
            result.append(node.val)

            # Traverse the right subtree
            if node.right: 
                dfs(node.right)

        # DFS to perform an inorder traversal of the tree starting at the root node
        dfs(root)
        
        return result
