# MY SOLN close but erroneous as we are actually not covering all the cases
# We need to optimize not completely discard the brute force, meaning we will still hacve some dead cases that we will need to look into
#  This again is not good but close, This file only serves as a purpose as to where you went wrong, which is 
# "We Nee to move the left pointer if we see anything lower that our current left"
# You might be wondering well why should I move to the lowest, I might lose data, well yes you will if you do not traverse to the end per every lower move and sav the profit value that you have encountered

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2):
            return 0
        start = 0
        end = 1
        profit = 0
        if(prices[end] - prices[start] > 0):
            profit = prices[end] - prices[start]
        print("profit: "+ str(profit) + "(start,end) " + str(start) + "," + str(end))
        for ptr in range (2,len(prices)):
            if(prices[ptr] - prices[end] >= profit and prices[ptr] - prices[end] >= prices[ptr] - prices[start] ):
                profit = prices[ptr] - prices[end]
                start = end
                end = ptr
                
                print("profit: "+ str(profit) + "(start,end) " + str(start) + "," + str(end))
            if(prices[ptr] - prices[start] >= profit and prices[ptr] - prices[start] >= prices[ptr] - prices[end] ):
                profit = prices[ptr] - prices[start]
                end = ptr
                
                # print("profit: "+ profit + "(start,end)" + [start,end])
                print("profit: "+ str(profit) + "(start,end) " + str(start) + "," + str(end))
        lowest = prices[start]
        for i in range(0,end):
            if(prices[i] < prices[start] and prices[i]<lowest):
                lowest = prices[i]
                profit = prices[end] - lowest
        
        
        return profit
            
        
