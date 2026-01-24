 class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = defaultdict(int) # student sandwich preferences: count

        # Count the total number of sandwiches the total body of students will eat
        for student in students:
            counts[student] += 1

        # Rather than adding the students to a queue and simulating them potentially repeatedly moving to the back of the line,
        # we actually only need to track the number of sandwiches that will be eaten.
        for sandwich in sandwiches:
            if counts[sandwich] > 0: # If there is still a student to eat the sandwich, mark it as eaten
                counts[sandwich] -= 1
            else: # Eventually one of the stacks of sandwiches will reach 0, in which case every student that will only eat that sandwich will remain unfed
                return counts[0] + counts[1]

        # If we get here every student successfully ate a sandwich
        return 0
