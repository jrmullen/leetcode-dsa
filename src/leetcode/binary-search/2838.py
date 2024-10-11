class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        result = [0] * len(heroes)
        # Combine the monster and coin values into a tuple and sort them by ascending monster value
        monsterCoins = sorted(zip(monsters, coins))
        
        # Populate a prefix sum of coins at each index
        prefix = [0] * len(monsterCoins)
        prefixSum = 0
        for i, (_, coin) in enumerate(monsterCoins):
            prefixSum += coin
            prefix[i] = prefixSum
        
        # Iterate over the list of heroes, find the strongest monster they can defeat, and add the coins earned to the `result` list
        for i, hero in enumerate(heroes):
            # Binary search to find the coin value prefix of the strongest monster the hero can defeat
            l, r = 0, len(monsterCoins) - 1
            while l <= r:
                mid = l + (r - l) // 2
                monster, _ = monsterCoins[mid]
                if hero >= monster:
                    l = mid + 1
                else:
                    r = mid - 1
            if l == 0 and monster > hero:
                continue # Edge case - if the hero can't defeat any monsters, default to 0 coins
            else:
                # When the strongest monster that hero can defeat is found, add the prefix sum of coins earned to the `result` list
                result[i] = prefix[r]
 
        return result
