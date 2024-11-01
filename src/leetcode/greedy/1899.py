class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = second = third = False
        targetX, targetY, targetZ = target

        for (x, y, z) in triplets:
            # If any of the values in the triplet are larger than any target value, it will never be a valid triplet
            if x > targetX or y > targetY or z > targetZ:
                continue

            # Otherwise, if there exists a triplet whose value is equal to a `target` value, track it
            if x == targetX:
                first = True
            if y == targetY:
                second = True
            if z == targetZ:
                third = True

            # If all target values are found, there exists a merge to create the `target` triplet
            if first and second and third:
                return True
        
        # If no solution was found, return False
        return False
