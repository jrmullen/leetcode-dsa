class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        result = [False] * len(queries)

        # First, build an adjacency list
        adj = { i: [] for i in range(numCourses)} # course: [pre-requisites]
        for prereq, course in prerequisites:
            adj[course].append(prereq)

        prereqMap = defaultdict(set) # { course: set of prerequisite courses }

        def dfs(course):
            # If the `course` has already been DFS'd, immediately return the result
            if course not in prereqMap:
                # Add the direct prerequisite `course` to the map
                prereqMap[course].add(course)
                for prereq in adj[course]:
                    # Add the prerequisites of each `prereq` returned by the DFS
                    prereqMap[course].update(dfs(prereq)) # `update()` combines 2 sets into 1
            
            # Finally, return all of the saved prerequisites for the course
            return prereqMap[course]
        
        # Second, DFS starting at each `course` to find all of the prerequisites for each course.
        # Results are saved in the `prereqMap` to avoid duplicate work
        for course in range(numCourses):
            dfs(course)
        
        # Evaluate each query using the `prereqMap`
        for i, (u, v) in enumerate(queries):
            result[i] = u in prereqMap[v]

        return result
