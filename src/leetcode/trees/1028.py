# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        dashes = 0
        i = 0

        while i < len(traversal):
            # If it's a dash, increment the `dashes` counter
            if traversal[i] == '-':
                dashes += 1
                i += 1
                continue 

            # Parse the `num` value from the `traversal` string
            j = i + 1
            while j < len(traversal) and traversal[j] != '-':
                 j += 1

            # Create the new node to insert into the tree
            num = int(traversal[i:j])
            newNode = TreeNode(num)
            
            # If necessary, `pop()` from the stack until the top of the stack is the correct "level" of the tree
            while len(stack) > dashes:
                stack.pop()

            # If there is a node on the stack, add the `newNode` as a child
            if stack:
                parent = stack[-1]
                # the `newNode` will be the left child unless there already is one
                if parent.left:
                    parent.right = newNode
                else:
                    parent.left = newNode
            
            # Move the `i` pointer forward
            i = j

            # Reset the `dashes` counter
            dashes = 0
                    
            # Finally, add the `newNode` to the stack
            stack.append(newNode)

        # The root node will never be popped off the stack, so it should always be in the first position of the list
        return stack[0]
