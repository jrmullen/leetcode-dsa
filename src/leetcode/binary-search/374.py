# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n

        # Binary search until the number is found, or the pointers cross
        while l <= r:
            mid = l + (r - l) // 2
            guess_result = guess(mid)
            if guess_result == 1:
                l = mid + 1 # The number is lower, so move the left pointer in
            elif guess_result == -1:
                r = mid - 1 # The number is higher, so move the right pointer in
            else:
                return mid # The number was found

        # Not found - shouldn't be possible given the constraints
        return -1
