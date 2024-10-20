class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # Base case - if `n` is 1, the value will always be 0
        if n == 1:
            return "0"
        
        # Calculate the length of the string
        length = 2 ** n

        # If `k` is in the left half of the string recurse with n-1
        if k < length // 2:
            return self.findKthBit(n - 1, k)
        
        # If `k` is in the right half of the string, find the corresponding bit on the left side and invert it
        if k > length // 2:
            # `length - k` will give the distance of `k` from the end of the string. The corresponding bit on the left side
            # would be the same distance from the start of the string
            correspondingBit = self.findKthBit(n - 1, length - k)
            return "0" if correspondingBit == "1" else "1" # Return the inverse value

        
        # If `k` is directly in the middle the value will always be 1
        if k == length // 2:
            return "1"
