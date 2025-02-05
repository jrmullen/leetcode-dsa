class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # 2 columns - index 1 for the buying scenario, and index 0 for the sell scenario
        # `n + 2` rows - `n` to account for each day's price, and 2 extra padded rows on the end to
        # make the DP logic simpler
        dp = [[0] * 2 for _ in range(n + 2)]

        # Start at the last day and work backwords, calculating the maximum buy/sell price at each point
        for i in range(n - 1, -1, -1):
            # Consider both the buy and sell scenarios for each position `i`
            for isBuying in [True, False]:
                if isBuying:
                    # Buying - buy the stock this day. The next state will be selling starting from the next index `i + 1`
                    buy = dp[i + 1][not isBuying] - prices[i]
                    # Cooldown - do nothing, forward the buy to the next day, index `i + 1`
                    cooldown = dp[i + 1][isBuying]
                    dp[i][1] = max(buy, cooldown)
                else:
                    # Selling - sell the stock this day. The next state will be buying starting from the next index `i + 1`
                    sell = dp[i + 2][not isBuying] + prices[i]
                    # Cooldown - do nothing, forward the sell to the next day, index `i + 1`
                    cooldown = dp[i + 1][isBuying]
                    dp[i][0] = max(sell, cooldown)
        
        return dp[0][1]
