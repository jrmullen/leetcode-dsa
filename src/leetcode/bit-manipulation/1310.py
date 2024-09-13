class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        pxor = [0] * (len(arr) + 1) # Copy the `arr` list as `px` to calculate the list's prefix sum

        # Populate `pxor` with the XOR of each element of `arr`
        for i in range(len(arr)):
            pxor[i + 1] = pxor[i] ^ arr[i]

        # Iterate through each query and compute its XOR value
        for q in queries:
            l, r = q
            # `pxor[l]` will contain the sum of all XORs up to element `l`
            # `pxor[r + 1]` will contain the sum of all XORs up to element `r + 1`
            # Therefore `pxor[r + 1] ^ pxor[l]` would isolate the XOR of only `l` to `r`
            result.append(pxor[r + 1] ^ pxor[l])

        return result
