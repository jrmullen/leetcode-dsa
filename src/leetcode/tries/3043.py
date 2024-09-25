class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        longest = 0
        prefixes = set()

        # Iterate over `arr1` and add all of its possible prefixes to a HashSet for efficient comparison
        for num in arr1:
            while num:
                prefixes.add(num)
                num //= 10 # Remove the last digit
        
        # Iterate over `arr2` and compare each prefix to the  `prefixes` set to find the longest
        for num in arr2:
            while num:
                if num in prefixes:
                    longest = max(longest, len(str(num))) # Track the longest prefix encountered
                    # Since digits are removed from the end, break immediately after finding a match since all proceeding values will be less digits
                    break
                num //= 10 # Remove the last digit

        return longest
