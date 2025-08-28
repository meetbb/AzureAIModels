"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    # Create three variables to store minimum value, profit and length of the input prices
    min = prices[0]
    profit = 0
    pricesLength = len(prices)
    
    for i in range(pricesLength):
        if (prices[i] < min):
            min = prices[i]
        profit = max(profit, prices[i] - min)
    return profit

print(maxProfit([7,1,5,3,6,4]))