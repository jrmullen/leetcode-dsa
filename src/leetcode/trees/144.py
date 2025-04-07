# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # Preorder traversal: root, left, right
        def dfs(node):
            # Base case: the current `node` is empty
            if not node:
                return
            
            result.append(node.val) # Append the value of the current `node` to the `result` list
            dfs(node.left) # Recurse down the left subtree
            dfs(node.right) # Recurse down the right subtree
        
        # DFS to perform a preorder traversal of the tree
        dfs(root)

        return result
