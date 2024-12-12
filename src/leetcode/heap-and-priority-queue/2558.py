class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Push the list of gifts into a max heap
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        # Perform the action `k` times
        for _ in range(k):
            pile = -heapq.heappop(gifts) # Pop the largest `pile` off the heap of `gifts`
            pile = math.isqrt(pile) # `isqrt()` calculates the integer square root, taking the floor
            heapq.heappush(gifts, -pile) # Push the `pile` back into the heap
        
        # Return the positive sum of the list of `gifts`
        return -sum(gifts)
