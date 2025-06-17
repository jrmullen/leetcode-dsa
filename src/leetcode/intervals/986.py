class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            start1, end1 = firstList[i]
            start2, end2 = secondList[j]

            # If the intervals are overlapping
            if start1 <= start2 <= end1 or start2 <= start1 <= end2:
                # The overlapping interval will begin at the lastest start time and end at the earliest end time
                start = max(start1, start2)
                end = min(end1, end2)
                result.append([start, end]) # Push the interval into the `result` list

            # Move the interval with the earliest end time forward
            if end1 < end2:
                i += 1
            else:
                j += 1

        return 