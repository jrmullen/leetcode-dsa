class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word) -> None:
        currentNode = self.root

        # Add the characters from `word` to the prefix tree
        for c in word:
            if c not in currentNode.children:
                currentNode.children[c] = TrieNode()
            currentNode = currentNode.children[c]

        # Mark the final character as the end of a word
        currentNode.isEndOfWord = True

    def containsPrefixes(self, word):
        currentNode = self.root

        # If every character of the word is not a word in the `words` list, return False
        for c in word:
            if c not in currentNode.children or not currentNode.children[c].isEndOfWord:
                return False
            currentNode = currentNode.children[c]
        return True


class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ''
        prefixTree = Trie()

        # Add each word from the `words` list to the Prefix Tree
        for word in words:
            prefixTree.insert(word)
        
        for word in words:
            # If the `word` is shorter than the current `result` it can be skipped
            if len(word) < len(result):
                continue
            if prefixTree.containsPrefixes(word):
                if len(word) > len(result):
                    result = word
                elif len(word) == len(result): # If the `word` is the same length as the `result`, keep the one that is lexicographically smaller
                    result = min(word, result)

        return result
