class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: # Sort in reverse order
            time = (target - p) / s
            if len(stack) >= 1 and stack[-1] >= time:
                continue
            stack.append(time)

        return len(stack)
