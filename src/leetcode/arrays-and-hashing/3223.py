class Solution:
    def minimumLength(self, s: str) -> int:
        result = 0
        
        # Get the count of characters in the string `s` and iterate over the values
        for count in Counter(s).values():
            # If there are an even number of characters the "process" will be performed
            # until there are 2 characters remaining. If it's odd it will be performed until
            # there is 1 character remaining.
            # e.g. if there are 4 characters and 2 are eliminated (left and right), 2 characters will remain.
            #      if there are 3 characters and 2 are eliminated (left and right), 1 character will remain.
            if count % 2 == 0:
                result += 2
            else:
                result += 1

        return result
