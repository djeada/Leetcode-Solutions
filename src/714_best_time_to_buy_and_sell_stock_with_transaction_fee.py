class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # profit_not_holding: max profit so far if we are *not* holding a share
        # profit_holding: max profit so far if we *are* holding a share
        profit_not_holding = 0
        profit_holding = -prices[0]  # if we buy on day 0
        
        for price in prices[1:]:
            # Option A: sell today (if we were holding), pay fee
            new_not_holding = max(
                profit_not_holding,          # do nothing
                profit_holding + price - fee # sell today
            )
            # Option B: buy today (if we were not holding)
            new_holding = max(
                profit_holding,              # do nothing
                profit_not_holding - price   # buy today
            )
            
            profit_not_holding, profit_holding = new_not_holding, new_holding
        
        # At the end, best is with no stock in hand
        return profit_not_holding
