class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # If `arr` does not have an even number of elements, immediately return `False`
        if len(arr) % 2 != 0:
            return False
        
        remainders = [0] * k

        # Calculate the remainder of each element of `arr` when divided by `k` and track a count
        for i in arr:
            remainders[i % k] += 1

        # Numbers with a remainder of 0 must be paired with themselves, so there must be an even number
        if remainders[0] % 2 != 0:
            return False

        # Compare non-zero remainders with their pair. rA = k - rB
        for i in range(1, len(remainders)):
            if remainders[i] != remainders[k - i]:
                return False

        return True
