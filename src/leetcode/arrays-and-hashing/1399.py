class Solution:
    def countLargestGroup(self, n: int) -> int:
        result = 0 # Number of groups with the largest size
        groups = defaultdict(int) # size: count
        biggest = 0 # Track the largest size

        # Iterate over each number from 1 to `n`
        for number in range(1, n + 1):
            total = 0 # Sum the digits
            for num in str(number):
                total += int(num)
            
            groups[total] += 1 # Increment the count of groups with the `total` sum
            biggest = max(biggest, groups[total]) # Update `biggefst` to track the largest size encountered
        
        # Iterate over each group and increment the `result` counter for each group that has a size equal to the `biggest` size
        for _, count in groups.items():
            result += 1 if count == biggest else 0
        
        return result
