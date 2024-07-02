class TrieNode:
    def __init__(self):
        self.isEndOfWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                # Update the pointer
                currentNode = currentNode.children[c]
            else:
                # Add a new node and update the pointer to point to the new node
                currentNode.children[c] = TrieNode()
                currentNode = currentNode.children[c]
        # Flag the last node as the end of a word
        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return False
        # If the final node is flagged as the end of the word we return True
        return currentNode.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root

        # If a character in `prefix` is not found, return False
        for c in prefix:
            if c in currentNode.children:
                currentNode = currentNode.children[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
