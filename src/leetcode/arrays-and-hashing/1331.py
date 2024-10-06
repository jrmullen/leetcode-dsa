class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []

        # De-dupe by adding to a set, and sort to easily determine the rank of each number
        sortedNums = sorted(set(arr))
        ranks = defaultdict(int)
        rank = 1

        # Map each number to its rank
        for n in sortedNums:
            ranks[n] += rank
            rank += 1
        
        # Iterate over `arr` and replace its values with their respective ranks
        for i, n in enumerate(arr):
            arr[i] = ranks[n]
        
        return arr
