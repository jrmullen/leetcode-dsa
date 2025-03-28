class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Base case: if there are not at least `n - 1` pairs in `trust`, exit immediately
        if len(trust) < n - 1:
            return -1
        
        # Track the number of incoming and outgoing edges for each person
        incoming = [0] * (n + 1) # inclusive `n`
        outgoing = [0] * (n + 1)

        # Iterate over each pair in `trust`, counting the incoming and outgoing edges
        for a, b in trust:
            outgoing[a] += 1
            incoming[b] += 1

        # Iterate over each value from 1 to `n`
        for i in range(1, n + 1):
            # Everyone in town must trust the town judge, except for himself, so the judge must have `n-1` incoming edges
            # The town judge must also trust no one, so the judge must have 0 outgoing edges
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i
        
        return -1
