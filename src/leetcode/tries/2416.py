class TrieNode:
    def __init__(self):
        self.count = 1 # New nodes are added with a default count of `1`
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Insert a new `word` into the Prefix Tree
    def insert(self, word) -> None:
        currentNode = self.root
        for c in word:
            if c in currentNode.children:
                # Update the pointer and increment the `count` of the existing node
                currentNode = currentNode.children[c]
                currentNode.count += 1
            else:
                # Add a new node and update the pointer to point to the new node
                currentNode.children[c] = TrieNode()
                currentNode = currentNode.children[c]

    # Calculate the score of the `word`
    def getScore(self, word) -> int:
        currentNode = self.root
        score = 0
        for c in word:
            currentNode = currentNode.children[c]
            score += currentNode.count
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result = []
        prefixTree = Trie()

        # Iterate over each word and add its characters to the `prefixTree`
        for word in words:
            prefixTree.insert(word)
        
        # Iterate over each word and populate the `result` with each word's score
        for word in words:
            result.append(prefixTree.getScore(word))

        return result
