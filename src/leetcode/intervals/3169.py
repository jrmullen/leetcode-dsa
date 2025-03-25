class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Sort the meetings in ascending order by start time
        meetings.sort()
        prev_end = 0 # Track the ending time of the previous meeting

        # Iterate over each
        for start, end in meetings:
            start = max(start, prev_end + 1) # To account for overlap, start at the latest ending time between `start` and the day after `prev_end`
            length = end - start + 1 # Calculate the number of days the meeting will require
            days -= max(length, 0) # Subtract the `length` of the meeting from the number of available `days`, ignoring negatives
            prev_end = max(prev_end, end) # Finally, update the `prev_end` pointer to point at the latest end time
        
        # Return the remaining available days
        return days
