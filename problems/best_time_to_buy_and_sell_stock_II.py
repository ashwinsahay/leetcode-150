""" 
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""




"""

Approach
To maximize profit, we can take advantage of every price increase. The key idea is to add up all the "uphill" (increasing) differences in price because each increase represents a potential profit.

Steps:
Identify Profitable Price Changes: Loop through the prices list and add the difference between consecutive days whenever there’s an increase (i.e., prices[i] > prices[i - 1]).
Accumulate Profit: If the price on day i is higher than on day i-1, it means that holding the stock from day i-1 to day i would yield a profit. We add this difference to our total profit.
Ignore Price Drops: If the price drops or stays the same, we ignore it, as it wouldn’t contribute to the profit.
This approach ensures that you capture every possible profit opportunity without explicitly simulating each buy-sell transaction.

Example Walkthrough
Example 1:
Input: prices = [7,1,5,3,6,4]
Process:
From day 1 to day 2, price drops (7 → 1), so we do nothing.
From day 2 to day 3, price increases (1 → 5), so we buy at 1 and sell at 5, earning a profit of 
5
−
1
=
4
5−1=4.
From day 3 to day 4, price drops (5 → 3), so we do nothing.
From day 4 to day 5, price increases (3 → 6), so we buy at 3 and sell at 6, earning a profit of 
6
−
3
=
3
6−3=3.
From day 5 to day 6, price drops (6 → 4), so we do nothing.
Total Profit: 
4
+
3
=
7
4+3=7
Example 2:
Input: prices = [1,2,3,4,5]
Process:
Every day the price increases:
Buy at 1, sell at 2, profit = 1.
Buy at 2, sell at 3, profit = 1.
Buy at 3, sell at 4, profit = 1.
Buy at 4, sell at 5, profit = 1.
Total Profit: 
1
+
1
+
1
+
1
=
4
1+1+1+1=4
Example 3:
Input: prices = [7,6,4,3,1]
Process:
Prices only decrease, so there’s no opportunity to make a profit.
Total Profit: 
0
0


"""




def maxProfit(prices):
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    return total_profit


"""
Complexity
Time Complexity: 
𝑂(𝑛)
O(n), where 
n is the number of days. We only need one pass through the prices list.
Space Complexity: 
𝑂
(1)
O(1), as we are only using a fixed amount of extra space.

"""