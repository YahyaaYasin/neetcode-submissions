class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l,r=0,1           #left will track the buy price and right will be the sell price
        profit=0

        while r<len(prices):

            if prices[l] < prices[r]:
                difference=prices[r]-prices[l]
                profit=max(difference, profit)
            else:
                l=r
            r+=1
        
        return profit





            