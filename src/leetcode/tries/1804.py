class TreeNode:
    def __init__(self):
        self.children = {}
        self.wordCount = 0 # Count the number of instances the word has been `insert()`ed
        self.prefixWordCount = 0 # Track the number of words starting at the node


class Trie:
    def __init__(self):
        self.root = TreeNode()

    # Inserts the string `word` into the trie
    def insert(self, word: str) -> None:
        currentNode = self.root
        for c in word:
            if c in currentNode.children: # If there's an existing node, use it. Otherwise create a new Node for the letter
                currentNode = currentNode.children[c]
            else:
                currentNode.children[c] = TreeNode()
                currentNode = currentNode.children[c]
            currentNode.prefixWordCount += 1 # Increment the prefix word count for each Node
        currentNode.wordCount += 1 # Increase the word count for the final Node
        
    # Returns the number of instances of the string `word` in the trie
    def countWordsEqualTo(self, word: str) -> int:
        currentNode = self.root
        for c in word:
            if c not in currentNode.children:
                return 0 # The word does not exist in the Prefix Tree, so return 0
            currentNode = currentNode.children[c]
        return currentNode.wordCount

    # Returns the number of strings in the trie that have the string `prefix` as a prefix
    def countWordsStartingWith(self, prefix: str) -> int:
        currentNode = self.root
        for c in prefix:
            if c not in currentNode.children:
                return 0 # The word does not exist in the Prefix Tree, so return 0
            currentNode = currentNode.children[c]
        return currentNode.prefixWordCount
    
    # Erases the string `word` from the trie
    def erase(self, word: str) -> None:
        currentNode = self.root
        for c in word:
            currentNode = currentNode.children[c]
            currentNode.prefixWordCount -= 1 # Decrease the prefix word count for each Node
        currentNode.wordCount -= 1 # Decrease the word count for the final Node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
