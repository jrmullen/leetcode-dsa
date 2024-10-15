class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        start = end = nums[0][0]
        result = [start, end]
        heap = []

        # Push the first element from each list into a heap and track the largest and smallest number among them
        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0)) # number, list index (row), number index (column)
            start = min(start, nums[i][0])
            end = max(end, nums[i][0])
        
        # Move the pointer of the list with the smallest value forward until one of the end of one of the lists is reached
        while len(heap) == len(nums):
            # Pop the smallest number off the heap and move it's list's pointer forward
            number, row, column = heapq.heappop(heap)
            column += 1

            # If the end of the row has not been reached, move the pointer forward
            if len(nums[row]) > column:
                # Pull the next number from the list containing the previous smallest number
                nextNumber = nums[row][column]
                # Re-calculate the largest number encountered to include the new value
                end = max(end, nextNumber)
                # Push the new value onto the heap and update the smallest current value
                heapq.heappush(heap, (nextNumber, row, column))
                start = heap[0][0]

            # If the new range is smaller than the previous smallest range, update the start and end values
            if end - start < result[1] - result[0]:
                result = [start, end]
        
        return result
