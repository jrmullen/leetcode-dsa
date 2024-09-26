class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
    

    # Insert a `word` into the Prefix Tree
    def insert(self, word) -> None:
        currentNode = self
        for c in word:
            if c in currentNode.children:
                # Update the pointer
                currentNode = currentNode.children[c]
            else:
                # Insert a new node for the missing character
                currentNode.children[c] = TrieNode()
                currentNode = currentNode.children[c]
        # Mark the end of the word
        currentNode.isEndOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()
        visited = set()
        prefixTree = TrieNode()
        ROWS = len(board)
        COLS = len(board[0])

        # Populate the `prefixTree` with the list of `words`
        for word in words:
            prefixTree.insert(word)
        
        def dfs(row, col, node, word) -> None:
            # Base case - do not continue if the tile is out of bounds, has already been visited,
            # or the character is not in the Prefix Tree
            if (row < 0 or row == ROWS
                or col < 0 or col == COLS 
                or (row, col) in visited
                or board[row][col] not in node.children):
                return
            
            # Mark the tile as visited
            visited.add((row, col))

            # Update the `node` and `word` to account for the new tile's character
            char = board[row][col]
            node = node.children[char]
            word += char
            
            # If the current letter is the last character of a target word, add the word to the `result` list
            if node.isEndOfWord:
                result.add(word)
            
            # Continue to neighboring tiles
            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)
            
            # Mark the tile as unvisited for future iterations
            visited.remove((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, prefixTree, '')

        return list(result)
