# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # Preorder traversal -> NODE, LEFT, RIGHT
        # This means that the first element of the `preorder` array will always be the root node
        root = TreeNode(preorder[0])

        # Find the index of the root value in the `inorder` array
        # Inorder traversal -> LEFT, NODE, RIGHT
        # Everything BEFORE the `nodeIndex` is the inorder left subtree
        # Everything AFTER the `nodeIndex` is the inorder right subtree
        nodeIndex = inorder.index(root.val)

        # Preorder - element 0 was the root node. Everything after that up to AND INCLUDING the `nodeIndex` is the left subtree
        # Inorder - Everything from the start of the array up to the `nodeIndex` is the left subtree
        root.left = self.buildTree(preorder[1: nodeIndex + 1], inorder[:nodeIndex])

        # Preorder - Everything after the `nodeIndex` to the end of the array is the right subtree
        # Inorder - Everything after the `nodeIndex` to the end of the array is the right subtree
        root.right = self.buildTree(preorder[nodeIndex + 1:], inorder[nodeIndex + 1:])

        # Return the tree that was build
        return root
