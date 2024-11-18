class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        N = len(code)
        result = [0] * N

        # If `k` is `0` there is no additional work to be done
        if k == 0:
            return result

        l = 0
        total = 0

        # Sliding window - note all values are modded `% N` to account for the circular array 
        for r in range(N + abs(k)):
            total += code[r % N]

            # If the window exceeds size `k`, the left pointer `l` must be shifted
            if r - l + 1 > abs(k):
                total -= code[l]
                l = (l + 1) % len(code)
            
            # If the window is of size `k` update the `result` list with the current `total`
            if r - l + 1 == abs(k):
                if k > 0:
                    result[(l - 1) % N] += total
                elif k < 0:
                    result[(r + 1) % N] += total

        return result
