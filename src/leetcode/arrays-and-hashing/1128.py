class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        result = 0
        seen = defaultdict(int) # Count the number of times a sorted domino pair is seen

        # Iterate over each domino in the list
        for a, b in dominoes:
            # First, sort the pair so the smaller value is always first
            pair = tuple(sorted([a, b])) # Tuple is immutable so must sort first, then cast

            # If the pair has already been seen, increase the `result` count
            if pair in seen:
                result += seen[pair] # Each duplicate domino previously can be paired with the new domino
            seen[pair] += 1 # Increment the `seen` counter

        return result
