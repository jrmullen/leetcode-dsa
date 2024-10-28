class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Base case: if the total amount of gas is less than the total cost, there will never be enough gas to complete a circuit
        if sum(gas) < sum(cost):
            return -1

        startIdx = 0
        totalGas = 0

        for i in range(len(gas)):
            # Calculate the difference between `gas` and `cost`.
            # Another way to think of it is adding the `gas` to the total, but subtracting the `cost` to get to the next station
            totalGas += (gas[i] - cost[i])

            # If the `totalGas` ever dips below 0, that `startIdx` will not work.
            if totalGas < 0:
                totalGas = 0 # Reset the count
                startIdx = i + 1 # Try again starting at the next `startIdx`

        return startIdx
