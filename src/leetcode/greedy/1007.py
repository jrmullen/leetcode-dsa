class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Helper function
        def get_min_rotations(target):
            top_rotations = bottom_rotations = 0
            for i in range(len(tops)):
                # If neither top or bottom values are the target, it will be impossible to have an equal row
                if tops[i] != target and bottoms[i] != target:
                    return -1 # Exit immediately
                
                # Now either the top or bottom must be equal to the target
                if tops[i] != target:
                    top_rotations += 1 # If the top is not the target value, rotate
                elif bottoms[i] != target:
                    bottom_rotations += 1 # If the bottom is not the target value, rotate

            # Finally, return the lowest required number of rotations
            return min(top_rotations, bottom_rotations)
        

        rotations = get_min_rotations(tops[0]) # Find the minimum number of rotations required to get the top side value at index 0

        # If a valid number of rotations is found, or if the top and bottom sides of the domino have the same value, return the minimum `rotations`
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else: # Otherwise, try re-calculate the minimum rotations using the bottom side domino value at index 0
            return get_min_rotations(bottoms[0])
