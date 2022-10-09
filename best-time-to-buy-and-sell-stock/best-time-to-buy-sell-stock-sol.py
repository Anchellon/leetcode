# DONT get mixed up with 2pt sol and keeping track of lowest val sol. I believe 2pt is more superior
Class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right =1
        maxP = 0
        while(right < len(prices)):
#             Check whether the transaction is profitable, if profitable calc profit and see if we can beat the maz profit , DONT MOVE left
            if(prices[right] - prices[left] > 0 ):
                profit = prices[right] - prices[left]
                maxP = max(maxP,profit)
#             If the transaction is not profitable move left to the new starting point at this lower price and see all profitable transactions from this point ( which woul occur in the next iteration)
            else:
                left = right
            right = right + 1    
        return maxP
                
