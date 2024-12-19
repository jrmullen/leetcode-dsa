class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        maximum = -1 # The minimum number of `arr` will be 0, so default to -1

        # Iterate over each number in the `arr`
        for i, num in enumerate(arr):
            # Intuition: track the maximum `num` encountered up to the current index. Since the goal is a sorted list,
            # and the `arr` is a permutation of a sorted list from `0` to `n-1`, each index `i` will match its number.
            # Therefore we can track the maximum number encountered, and if the current index `i` matches that number,
            # it must be a valid partition 
            maximum = max(maximum, num)
            if maximum == i:
                result += 1

        return result
