class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Buy on day0 and sell on day1
        ret_max = 0
        while r < len(prices): # We gonna shift the l-r window to the end
            if prices[r] - prices[l] > 0: # Profitable, compare to the previous profit
                ret_max = max(ret_max, prices[r] - prices[l])
                r = r+1 # keep seeing if there is more profit
            else: # Found the lower price to buy, shift the buy day to r
                l = r
                r = r+1
        return ret_max

