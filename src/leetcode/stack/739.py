class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # pair [index, temp]
        solution = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                solution[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, t])

        return solution
