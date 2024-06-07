class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                # Add a new node and update the pointer
                currentNode.children[c] = TrieNode()
                currentNode = currentNode.children[c]
        # Flag the last node as the end of a word
        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(k, node):
            currentNode = node

            # Iterate over all characters left in the word
            for i in range(k, len(word)):
                char = word[i]

                if char == '.':
                    # Run a DFS over each of the node's child nodes
                    for child in currentNode.children.values():
                        # If any of the children have a successful result we return True
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in currentNode.children:
                        return False
                    # Move the pointer forward
                    currentNode = currentNode.children[char]
            # Only return true if the final node is flagged as the end of a word
            return currentNode.isEndOfWord

        # Start at the first character of the word and the root note
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
