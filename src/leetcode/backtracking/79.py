class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        used = set()

        def backtrack(h, w, c):
            # Base case
            if c == len(word):
                return True

            if (h >= height or h < 0 or w >= width or w < 0  # Tile is out of bounds
                    or board[h][w] != word[c]  # Tile does not contain the target letter
                    or (h, w) in used):  # Character has already been used
                return False

            # Actions - check all adjacent tiles
            used.add((h, w))
            answer = (backtrack(h, w - 1, c + 1) or backtrack(h, w + 1, c + 1)
                      or backtrack(h - 1, w, c + 1) or backtrack(h + 1, w, c + 1))
            # Undo the above action
            used.remove((h, w))
            return answer

        # Iterate over each tile on the board
        for h in range(height):
            for w in range(width):
                if backtrack(h, w, 0):
                    return True

        return False
