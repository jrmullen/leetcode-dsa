class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Intuition: Hierholzer's Algorithm to find a Eulerian Path
        result = []

        # Construct an adjacency list `flights` after first sorting the list of `tickets` by LARGEST lexical order
        flights = defaultdict(list)
        for source, dest in reversed(sorted(tickets)):
            flights[source].append(dest)

        def dfs(source):
            # Visit all possible neighbors of the `source` node
            while flights[source]:
                # Pop the smallest lexical `dest` node from the `source` node's list of neighbors and perform a DFS
                dest = flights[source].pop()
                dfs(dest)

            # Finally, append the `source` node to the `result` list 
            result.append(source)
        
        # DFS beginning at JFK
        dfs('JFK')

        # Return the `result` list in reversed order
        return result[::-1]
