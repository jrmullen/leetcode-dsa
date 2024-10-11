class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Sort the `times` in ascending order, paired in a tuple with the associated friend (original index)
        times = [(arrive, leave, friend) for friend, (arrive, leave) in enumerate(times)]
        times.sort()

        # Populate two heaps to track the chairs that are available and the chairs that have been taken
        openChairs = [i for i in range(len(times))]
        filledChairs = [] # (leave, chair)

        for arrive, leave, friend in times:
            # Re-open chairs for friends that may have left before the current friend arrived
            while filledChairs and filledChairs[0][0] <= arrive:
                heapq.heappush(openChairs, heapq.heappop(filledChairs)[1])
            
            # Assign a chair to the currently arriving friend
            chair = heapq.heappop(openChairs)
            heapq.heappush(filledChairs, (leave, chair))

            # If the current `friend` is the `targetFriend`, return the seat that they were assigned
            if friend == targetFriend:
                return chair
