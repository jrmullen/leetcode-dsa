class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n

        setA = set()
        setB = set()

        for i in range(n):
            # Backfill the value of the current element in the `result` list with the previous element's value
            if i > 0:
                result[i] = result[i - 1]

            # Add the values to their associated sets
            setA.add(A[i])
            setB.add(B[i])

            # If the value from both lists are the same, increment the `result` count at the current index by 1
            if A[i] == B[i]:
                result[i] += 1
                continue

            # If the values of `a` and `b` are NOT the same, they must be checked individually
            if A[i] in setB:
                result[i] += 1
            
            if B[i] in setA:
                result[i] += 1

        return result
