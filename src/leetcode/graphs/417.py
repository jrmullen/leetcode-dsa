class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result = []
        visitedPacific = set()
        visitedAtlantic = set()
        rows = len(heights)
        columns = len(heights[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, visited, previousHeight):
            # Base case - tile out of bounds, smaller than the previous tile, or has already been visited
            if (r not in range(rows) or
                    c not in range(columns) or
                    heights[r][c] < previousHeight or
                    (r, c) in visited
            ):
                return

            # Mark the tile as visited
            visited.add((r, c))

            # Attempt to visit all neighboring tiles
            for dRow, dCol in directions:
                dfs(r + dRow, c + dCol, visited, heights[r][c])

        # Start at the tiles bordering each ocean and DFS backwards
        for r in range(rows):
            dfs(r, 0, visitedPacific, 0)  # Pacific
            dfs(r, columns - 1, visitedAtlantic, 0)  # Atlantic

        for c in range(columns):
            dfs(0, c, visitedPacific, 0)  # Pacific
            dfs(rows - 1, c, visitedAtlantic, 0)  # Atlantic

        # Iterate over every tile - if it is present in both `visited` sets, it is a valid tile
        for r in range(rows):
            for c in range(columns):
                if (r, c) in visitedPacific and (r, c) in visitedAtlantic:
                    result.append([r, c])

        return result
