class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # 3 stacks - one for >, <, = values compared with the `pivot` number
        less = []
        more = []
        equal = []

        # Iterate over each number from left to right
        for num in nums:
            # Compare the `num` with the `pivot` and place it into the correct bucket
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                equal.append(num)

        # Finally, squish all 3 lists together in order and return the result
        return less + equal + more
