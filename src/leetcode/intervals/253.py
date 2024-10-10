class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxRoomCount = 0
        roomCount = 0
        time = []

        # Create a list of tuples (time, count), where start times have a positive count and end times have a negative count
        for start, end in intervals:
            time.append((start, 1))
            time.append((end, -1))

        # Sort the list of times so they are in chronological order
        time.sort()

        # Iterate over each time tuple and adjust the time `count`. When a meeting starts, the `roomCount` will go up.
        # When a meeting ends, the meeting `roomCount`` will go down.
        # If multiple meetings start during the same time period, more meeting rooms will be required.
        # Update the `maxRoomCount` to track the largest number of simultaneous meetings needed
        for _, count in time:
            roomCount += count
            maxRoomCount = max(maxRoomCount, roomCount)
        
        return maxRoomCount
