class Solution:
    def alienOrder(self, words: List[str]) -> str:
        result = []
        adj = { c: set() for word in words for c in word }

        # Populate the adjacency list `adj` using pairs of sorted words from the list
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            minLength = min(len(word1), len(word2))

            # `word1` cannot be larger than `word2` while also being a substring of `word2`
            if len(word1) > len(word2) and word1[:minLength] == word2[:minLength]:
                return ''

            # Find the first differing character between the two words
            for j in range(minLength):
                # The first character in `word1` that differs from `word2` will be lexicographically smaller
                if word1[j] != word2[j]:
                    # Add the characters the adjacency list
                    adj[word1[j]].add(word2[j])
                    break

        # Post-order traversal DFS
        visited = {} # True - visited, false - in the current path
        def dfs(char):
            # Base case
            if char in visited:
                return visited[char]
            
            # Mark the current character as visited
            visited[char] = True

            # DFS on neighboring characters
            for neighbor in adj[char]:
                # If a node is re-visited in a DFS it means there is a cycle in the graph
                if dfs(neighbor):
                    return True

            # Finally, mark the character as part of the current path and add the character to the result
            visited[char] = False
            result.append(char)
        
        # DFS from each character in the adjacency list
        for c in adj.keys():
            # If the DFS ever returns true there is a cycle in the graph
            if dfs(c):
                return ''

        # Return the `result` string in reverse order
        return ''.join(result[::-1])
