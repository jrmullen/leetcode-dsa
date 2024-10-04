class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        result = 0
        total = 0
        count = defaultdict(int)
        numPairs = len(skill) // 2

        # Sum all elements in `n` and add their counts to the `count` map
        for n in skill:
            total += n
            count[n] += 1
        
        # If the `total` does not evenly go into the number of required groups (# of elements / 2 pairs), immediately return
        if total % numPairs:
            return -1
        
        for n in skill:
            # If the count of `n` is 0 in the `count` map, continue
            if not count[n]:
                continue
            
            # If the `target` number to be paired with `n` has a count of 0 in the `count` map, the team cannot be equally split
            target = (total // numPairs) - n
            if not count[target]:
                return -1

            # Update the `result` and decrement the `count` for the numbers used in the pair
            result += (n * target)
            count[n] -= 1
            count[target] -= 1
        
        return
