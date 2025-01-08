class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n

        left_balls = 0
        left_moves = 0
        right_balls = 0
        right_moves = 0

        for i in range(n):
            # Left pass
            result[i] += left_moves
            left_balls += int(boxes[i])
            left_moves += left_balls

            # Right pass
            j = n - 1 - i
            result[j] += right_moves
            right_balls += int(boxes[j])
            right_moves += right_balls
        
        return result
