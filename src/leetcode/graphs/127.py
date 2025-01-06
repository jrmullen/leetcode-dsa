class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        result = 0
        visited = set()
        edges = defaultdict(list)

        # If the `endWord` is not in the `wordList` return immeddiately
        if endWord not in wordList:
            return result
        
        # Build an adjacency list `edges` mapping each `pattern` to a list of matching words
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                edges[pattern].append(word)

        # BFS until the final word is found
        q = deque()
        q.appendleft(beginWord)
        visited.add(beginWord)

        while q:
            # Increment the `result` counter each time a "batch" of connected words are traversed
            result += 1

            # Snapshot everything currently on the queue
            for _ in range(len(q)):
                # Pop the next word off the queue
                word = q.pop()

                # If the `endWord` has been found, return the `result` count
                if word == endWord:
                    return result

                # Add each word `w` that matches the possible `pattern`s that can be created from the current `word`
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for w in edges[pattern]:
                        # If the `word` has already been visited, skip it
                        if w not in visited:
                            q.appendleft(w) # Add the matching word `w` to the `q`
                            visited.add(w) # Mark the matching word `w` as visited

        return 0
