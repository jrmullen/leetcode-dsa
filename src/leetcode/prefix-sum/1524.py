class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0
        current_sum = 0

        # Track the number of odd and even prefix sums
        odd_count = 0
        event_count = 0

        for num in arr:
            current_sum += num

            if current_sum % 2 == 0:
                # If the sum is even update the `event_count` and add the `odd_count` to the `result`
                event_count += 1
                result = (result + odd_count) % (10**9 + 7) # By removing all of the `even` prefix sums we are left with only the odd values

            else:
                # If the sum is odd increment the `result` by 1, but also account for all of the `even_count` prefixes
                # that could be removed to create odd prefix sums
                odd_count += 1
                result = (result + 1 + event_count) % (10**9 + 7)
        
        return result
