class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Node states
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        reqMap = { i:[] for i in range(numCourses) }
        nodes = [UNVISITED] * numCourses
        result = []

        # Populate `reqMap` with all of the courses and their prerequisites
        for course, prereq in prerequisites:
            reqMap[course].append(prereq)

        def dfs(course):
            # Base case
            if nodes[course] == VISITING:
                return False # If a node is reached that has already been visited, there is a cycle in the graph
            elif nodes[course] == VISITED:
                return True # If the node has already been marked as visited, the course can be completed

            # Mark the node as `VISITING`            
            nodes[course] = VISITING

            # Visit all prerequisite nodes
            for prereq in reqMap[course]:
                if not dfs(prereq):
                    return False # A cycle has been detected in the graph
            
            # The course is able to be completed
            nodes[course] = VISITED
            # Completable courses will be added to `result` in the order they can be finished in
            result.append(course)
            return True

        # Visit each course node and DFS each prerequisite
        for i in range(numCourses):
            if not dfs(i):
                return [] # A cycle has been detected in the graph - the courses are impossible to finish
        
        return result
