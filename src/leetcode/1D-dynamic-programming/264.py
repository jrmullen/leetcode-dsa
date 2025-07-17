class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1 # Base case: the first ugly number will always be 1

        p = q = r = 0 # 3 pointers to track the indices of the dp array to calculate the next ugly multiple
        
        # Track the next multiple of each prime 2, 3, 5
        next_two = 2
        next_three = 3
        next_five = 5

        for i in range(1, n):
            next_num = min(next_two, next_three, next_five) # Choose the smallest of the next possible 3 values
            dp[i] = next_num # Populate the dp array with the chosen number

            # Depending on which number was added to the dp array, update pointers and next multiples
            # Important to use an if statement for each case! e.g. 6 will be both a multiple of 2 and 3 at the same time
            if next_num == next_two:
                p += 1
                next_two = dp[p] * 2 # The next multiple of 2 will be the curent value multiplied by 2
            if next_num == next_three:
                q += 1
                next_three = dp[q] * 3 # The next multiple of 2 will be the curent value multiplied by 3
            if next_num == next_five:
                r += 1
                next_five = dp[r] * 5 # The next multiple of 5 will be the curent value multiplied by 5

        return dp[-1] # The last value of the array will be the nth ugly number
