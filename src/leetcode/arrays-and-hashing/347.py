class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # number: count

        for n in nums:
            count[n] = count.get(n, 0) + 1

        sort = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            sort[c].append(n)

        solution = []
        for i in range(len(sort) - 1, 0, -1):
            for j in sort[i]:
                solution.append(j)
                if len(solution) == k:
                    return solution
