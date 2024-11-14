class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []

        # Find the smallest and largest numbers across all 3 arrays
        lowest = min(arr1[0], arr2[0], arr3[0])
        highest = max(arr1[-1], arr2[-1], arr3[-1])

        # Convert each list to a set for efficient lookups
        s1, s2, s3 = set(arr1), set(arr2), set(arr3)

        # Iterate over each number `n` from `lowest` to `highest` (inclusive)
        for n in range(lowest, highest + 1):
            # If the number `n` is in all 3 sets, add it to the `result` list
            if n in s1 and n in s2 and n in s3:
                result.append(n)
        
        return result
