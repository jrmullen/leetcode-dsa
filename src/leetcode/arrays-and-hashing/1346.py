class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        visited = set() # Track each number

        for num in arr:
            # if the doubled value of `num` is in the `arr` or `num` is even and it's half is in the `arr`
            if num * 2 in visited or (num % 2 == 0 and num // 2 in visited):
                return True
            # Mark the `num` as visited
            visited.add(num)
        return False
