from sortedcontainers import SortedDict

class MyCalendarTwo:

    def __init__(self):
        self.singleBookings = []
        self.doubleBookings = []

    def book(self, start: int, end: int) -> bool:
        # Check if there is an overlapping double booking
        for doubleStart, doubleEnd in self.doubleBookings:
            if start < doubleEnd and end > doubleStart:
                return False # Would be a triple booking - return False

        # Check if there is an overlapping single booking
        for singleStart, singleEnd in self.singleBookings:
            if start < singleEnd and end > singleStart:
                # There is an overlapping time range, so add that segment to the `doubleBookings` list
                self.doubleBookings.append((max(start, singleStart), min(end, singleEnd)))

        # Book the event
        self.singleBookings.append((start, end))

        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)