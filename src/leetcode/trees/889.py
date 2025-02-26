# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:     
        # Map each value in the `postorder` list to its index for efficient lookups
        postorder_to_index = {}
        for i, n in enumerate(postorder):
            postorder_to_index[n] = i
        
        # Recursive function to build each sub-tree
        def build_tree(i1, i2, j1):
            # Base case: all nodes have been used, pointers cross
            if i1 > i2:
                return None
        
            # Create the node
            root = TreeNode(preorder[i1])

            # Don't recurse if both pointers are at the same node
            if i1 != i2:
                left_value = preorder[i1 + 1]

                # Pints to the index of the `left_value` in the `postorder` list
                mid = postorder_to_index[left_value]

                # The size will be the difference between the `mid` point and `j1`, offset by 1 to be inclusivve
                left_size = mid - j1 + 1

                # Recursively build the sub-trees until a leaf node is reached
                root.left = build_tree(i1 + 1, i1 + left_size, j1)
                root.right = build_tree(i1 + left_size + 1, i2, mid + 1)
            
            # Finally, return the `root` node
            return root

        # `i1` starts at the beginning of `preorder` list
        # `i2` starts at the end of `preorder` list
        # `j1` starts at the beginning of the `postorder` list
        return build_tree(0, len(preorder) - 1, 0)
