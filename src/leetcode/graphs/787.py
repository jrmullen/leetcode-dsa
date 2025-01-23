class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:     
        # Bellman-Ford algorithm
        prices = [float('inf')] * n
        prices[src] = 0 # Mark the starting city as having no cost

        # At most `k` stops means 2 edges may be included, so iterate k + 1 times
        for _ in range(k + 1):
            # Copy the pricing `prices` list
            pricesCopy = prices.copy()

            # Visit each node in the graph
            for source, dest, cost in flights:
                # If the cost to get to the `source` node is unknown, skip the node
                if prices[source] == float('inf'):
                    continue
                
                # Update the cost to get to the `dest` if a less expensive route has been found
                if prices[source] + cost < pricesCopy[dest]:
                    pricesCopy[dest] = prices[source] + cost
            
            # Finally, overwrite the original `prices` list with the updated `pricesCopy` list for the next iteration
            prices = pricesCopy
        
        # If the `dst` node does not have a price in the `prices` list, return the default value of -1
        return prices[dst] if prices[dst] != float('inf') else -1
