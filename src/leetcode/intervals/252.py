class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(len(intervals) - 1):
            start, end = intervals[i]
            nextStart = intervals[i + 1][0]

            # If the next interval starts before the current interval ends, they are overlapping
            if nextStart < end:
                return False
        return True
