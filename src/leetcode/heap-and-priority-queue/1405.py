class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ''

        # Create a max heap to track the letters by available count
        maxHeap = []
        if a: heapq.heappush(maxHeap, (-a, 'a'))
        if b: heapq.heappush(maxHeap, (-b, 'b'))
        if c: heapq.heappush(maxHeap, (-c, 'c'))

        while maxHeap:
            # Pop the largest value from the heap
            count, letter = heapq.heappop(maxHeap)

            # If there are already 2 of the same letter, the letter with the second highest count should be used instead
            if len(result) >= 2 and letter == result[-1] == result[-2]:
                # If there are no other letters to be used, break out of the loop to return
                if not maxHeap:
                    break

                # Pop the letter with the second largest count from the heap
                count2, letter2 = heapq.heappop(maxHeap)
                # # Add the letter with the second largest count first and decrement the count (max heap, so adding is decrementing)
                result += letter2
                count2 += 1

                # Add the letter with the second largest count back to the heap if it still has a count
                if count2:
                    heapq.heappush(maxHeap, (count2, letter2))
                
                # Add the letter with the largest count next and decrement the count (max heap, so adding is decrementing)
                result += letter
                count += 1
            else:
                result += letter
                count += 1

            # Add the letter with the largest count back to the heap if it still has a count
            if count:
                    heapq.heappush(maxHeap, (count, letter))

        return result
