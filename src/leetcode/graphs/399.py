class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        result = []
        graph = defaultdict(list)

        # Populate the `graph` with 
        for i, equation in enumerate(equations):
            a, b = equation
            graph[a].append([b, values[i]]) # a -> b (a / b), the value is already given
            graph[b].append([a, 1 / values[i]]) # b -> a (b / a), the value is the reciprocal
        
        def bfs(source, target):
            # If the `source` or `target` are not present in the graph
            # there's no way to calculate a value, so default to -1
            if source not in graph or target not in graph:
                return -1.0
            
            visited = set()
            q = deque()
            q.appendleft((source, 1))
            visited.add(source)
            while q:
                variable, val = q.pop()

                # If the target is found the variables are connected in the graph. Return the calculated product of all edges
                if variable == target:
                        return val
                
                # Visit each unvisited neighbor node and re=calculate the product of their values
                for neighbor, value in graph[variable]:
                    if neighbor not in visited:
                        product = value * val # Multiply the edge values to get the new product
                        q.appendleft((neighbor, product))
                        visited.add(neighbor) # Mark the node as visited
            
            # If the variables are not connected in the graph
            # # there's no way to calculate a value, so default to -1
            return -1.0
        
        # Run a BFS on each query to populate the `result` list
        for query in queries:
            x, y = query
            result.append(bfs(x, y))
        
        return result
