class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        result = 0
        prefixXOR = 0 # Default the XOR value to 0

        # Create a map to track the parity of each character
        charMap = [0] * 26
        # 5 vowels -> 5 bits -> 2^5 possible states
        # Map each vowel to its bitmask value in the `charMap`
        charMap[ord('a') - ord('a')] = 1
        charMap[ord('e') - ord('a')] = 2
        charMap[ord('i') - ord('a')] = 4
        charMap[ord('o') - ord('a')] = 8
        charMap[ord('u') - ord('a')] = 16
        # Create a map for tracking indexes
        indexMap = [-1] * 32

        for i, c in enumerate(s):
            # If a vowel appears an even number of times, the result of XOR will be 0; if it appears an odd number of times, the result will be 1
            prefixXOR ^= charMap[ord(c) - ord('a')]
            if indexMap[prefixXOR] == -1 and prefixXOR != 0:
                indexMap[prefixXOR] = i
            result = max(result, i - indexMap[prefixXOR])

        return result
