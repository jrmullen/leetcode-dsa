class Solution:
    def reorganizeString(self, s: str) -> str:
        result = []
        freq = defaultdict(int) 
        heap = [] # Max heap by inverting numbers to negative values

        # Count the number of times each character occurs in the string `s`
        for c in s:
            freq[c] += 1
        
        # Push the characters into a heap keyed on the frequency count
        for c, count in freq.items():
            heapq.heappush(heap, (-count, c)) # Push the values as negatives to order them by largest value first
        
        # If the most frequently occurring character takes of more than half of the available characters they cannot be successfully rearranged
        if len(s) - -heap[0][0] < -heap[0][0] - 1:
            return ''
        
        # Intuition: alternate between the two most frequently occurring characters and add them to the `result` list

        prev = None # Track the previously processed character
        while heap:
            count, c = heapq.heappop(heap)
            count = -count # Decrease the count
            result.append(c) # Push the character `c` into the `result` list

            # Push the previous character back onto the heap
            if prev:
                heapq.heappush(heap, prev)

            # Update the `prev` pointer to point at the current character for the next iteration
            prev = (-count + 1, c) if count - 1 > 0 else None
        
        # Finally, rejoin the `result` back into a string
        return ''.join(result)
