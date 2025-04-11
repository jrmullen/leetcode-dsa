class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        # Iterate over each number from `low` to `high`
        for num in range(low, high + 1):
            # Constraints: numbers must be between 1 and 10,000
            # If the num is a 2 digit number, it must be a multiple of 11 to be symmetric
            if num <= 99 and num % 11 == 0:
                result += 1
            
            # If the num is a 4 digit number, the left and right halves must have equal sums
            if num >= 1000 and num <= 9999:
                left = (num // 1000) + (num % 1000 // 100) # thousandths place + hundredths place
                right = (left % 100 // 10) + (num % 10) # Tens place + ones place

                # If the right and left halves have equal sums, they are symmetric
                result += 1 if left == right else 0

        return result
