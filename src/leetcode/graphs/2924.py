class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Count of number of `incoming` edges of each `destination` vertex in the list of `edges`
        incoming = [0 for _ in range(n)]
        for source, destination in edges:
            incoming[destination] += 1

        # Track the "champion" vertices
        champions = []
        for i, count in enumerate(incoming):
            # If the count of incoming edges is `0` for a vertex, that vertex is a champion
            if count == 0:
                champions.append(i)
        
        # If there is only a single `champion` vertex, return its value
        return -1 if len(champions) > 1 else champions[0]
