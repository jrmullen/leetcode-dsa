class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        t = 0

        for i in range(1, n + 1):
            result.append('Push') # Push the number onto the stack

            if i != target[t]: # If the number is not a target number, pop it off
                result.append('Pop')
                continue

            # If the final target number has been found, return immediately
            if t == len(target) - 1:
                return result

            # Otherwise move the pointer forward to the next target number
            t += 1
