# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Postorder traversal: left, right, root
        def dfs(node):
            # Base case: the `node` does not exist
            if not node:
                return

            # Traverse the left child node's tree
            if node.left:
                dfs(node.left)

            # Traverse the right child node's tree
            if node.right:
                dfs(node.right)

            # Finally, append the value of the node to the `result` list
            result.append(node.val)
        
        dfs(root) # DFS starting at the root node to perform postorder traversal
        return result
