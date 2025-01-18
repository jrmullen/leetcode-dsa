class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor = 0 # Start at 0 since anything XORed with 0 will be itself

        for n in derived:
            xor ^= n # XOR the current `xor` value with `n`
        
        # If the final cumulative XOR value is 0, there will exist a valid `original` list
        return xor == 0
