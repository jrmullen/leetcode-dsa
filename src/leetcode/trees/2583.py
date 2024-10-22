# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        sums = []

        # BFS to calculate the sum of each level
        q = deque()
        q.appendleft(root)
        while q:
            levelSum = 0

            # Pop each noded off the queue and add its value to the `levelSum`
            for _ in range(len(q)):
                node = q.pop()
                levelSum += node.val

                # Add leaf nodes to the queue if they are present
                if node.left:
                    q.appendleft(node.left) 
                if node.right:
                    q.appendleft(node.right)
            
            sums.append(-levelSum) # Negative number for minHeap

        # Return -1 if there are fewer than `k` levels in the tree
        if k > len(sums):
            return -1

        # Sort the list of sums and return the `k`th largest
        return -sorted(sums)[k - 1]
