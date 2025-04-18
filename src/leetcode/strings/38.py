class Solution:
    def countAndSay(self, n: int) -> str:
        current_string = '1' # Base case: countAndSay(1) = "1"
        
        # RLE encode the string n - 1 times
        for _ in range(n - 1):
            l = r = 0 # 2 pointers, both initially at the leftmost index of the current string
            next_string = '' # Placeholder empty string to build upon

            # Traverse the current string from left to right counting the number of neighboring duplicates
            while l < len(current_string):
                # Move the right pointer forward until a different number or the end of the string is encountered
                while r < len(current_string) and current_string[r] == current_string[l]:
                    r += 1
                
                # The number count will be the difference between the right and left pointers
                next_string += str(r - l) + current_string[l] # ppend the count and number to the next string
                l = r # Move the left pointer forward
            
            current_string = next_string # Update the current string to be the new string for the next iteration

        # Return the final string
        return current_string
