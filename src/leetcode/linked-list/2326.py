# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # In order: east, south, west, north
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0 # Default direction moves east
        x = 0 # Starting location is the Northwestern corner 0, 0
        y = 0

        # Populate an `m` by `n` matrix, defaulting each element to -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Iterate over the Linked List while populating `matrix` in a spiral
        while head is not None:
            matrix[x][y] = head.val # Populate the cell
            head = head.next # Progress `head`

            # If the next cell is out of bounds or is already populated with a value, update the direction
            newX = x + directions[direction][0]
            newY = y + directions[direction][1]
            if newX >= m or newX < 0 or newY >= n or newY < 0 or matrix[newX][newY] != -1:
                direction = (direction + 1) % 4 # Increment to the next direction, modding by 4 to loop back to 0
            
            x += directions[direction][0]
            y += directions[direction][1]

        return matrix
