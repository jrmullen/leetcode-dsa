class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Base case: `hand` cannot be evenly divided into `groupSize` groups
        if len(hand) % groupSize > 0:
            return False
        
        # Base case: if `groupSize` is 1, it should always be able to be split
        if groupSize == 1:
            return True
        
        # Count each card
        cardCount = defaultdict(int)
        for card in hand:
            cardCount[card] += 1

        # Sort the `hand` in ascending order
        heap = list(cardCount.keys())
        heapq.heapify(heap)

        while heap:
            start = heap[0] # Start with the smallest possible card since all values in the group must start at that value
            # Iterate over cards from `start` until `groupSize` cards has been checked
            for card in range(start, start + groupSize):
                # A card necessary for the straight is not in the hand
                if card not in cardCount:
                    return False
                
                # Otherwise, the card is in the hand
                cardCount[card] -= 1 # Decrease the count
                if cardCount[card] <= 0:
                    # If there are no `card` cards left in the hand (count is 0) remove it from the heap.
                    # If it's not the smallest card, 
                    if card != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True
