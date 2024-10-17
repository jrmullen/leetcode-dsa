class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        largest = "0"
        largestIndex = -1
        swapFromIndex = -1
        swapToIndex = -1

        # Iterate over the numbers in `num` from right to left
        for i in range(len(num) - 1, -1, -1):
            # The current number is smaller than the `largest` number. Save the indexes for a potential swap.
            # Each iteration will be comparing a more significant number
            if num[i] < largest:
                swapToIndex = i
                swapFromIndex = largestIndex
            
            # The current number is larger than the `largest` number. Update `largest` and `largestIndex` pointers
            if num[i] > largest:
                largest = num[i]
                largestIndex = i

        # Now perform the swap. The entire number has been scanned. `swapFromIndex` contains the index of the largest number.
        # `swapToIndex` contains the index of the most significant number that is smaller than the `largest` number
        num[swapFromIndex], num[swapToIndex] = num[swapToIndex], num[swapFromIndex]
        
        # Re-join into an integer and return
        return int(''.join(num))
