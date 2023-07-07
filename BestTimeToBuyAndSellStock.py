class Solution:
    """
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.
    """
    def maxProfit(self, prices: List[int]) -> int:
        maximum, l, r = 0, 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                curr = prices[r] - prices[l]
                maximum = max(maximum, curr)
            else:
                l = r
            r += 1
        return maximum