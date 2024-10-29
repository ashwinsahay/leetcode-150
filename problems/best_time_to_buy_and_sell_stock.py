# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.



class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #first find min element , this will be the lowest price

        # min_element=min(prices)
        # min_index=prices.index(min_element)

        # subset_list=prices[min_index+1:]

        # if len(subset_list)==0:
        #     return 0

        # max_element=max(subset_list) 

        # if max_element<=min_element:
        #     return 0
        # else:
        #     return max_element-min_element

        min_price = float('inf')
        max_profit = 0
    
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
    
        return max_profit


        

# Let's go through the solution step by step with the input [2, 8, 1, 3]:

# Initialize min_price to float('inf') and max_profit to 0.

# Iterate through the list of prices:

# First iteration (price = 2):
# Update min_price to the minimum of float('inf') and 2, which is 2.
# Calculate the potential profit: 2 - 2 = 0.
# Update max_profit to the maximum of 0 and 0, which is 0.
# Second iteration (price = 8):
# Update min_price to the minimum of 2 and 8, which is 2.
# Calculate the potential profit: 8 - 2 = 6.
# Update max_profit to the maximum of 0 and 6, which is 6.
# Third iteration (price = 1):
# Update min_price to the minimum of 2 and 1, which is 1.
# Calculate the potential profit: 1 - 1 = 0.
# Update max_profit to the maximum of 6 and 0, which is 6.
# Fourth iteration (price = 3):
# Update min_price to the minimum of 1 and 3, which is 1.
# Calculate the potential profit: 3 - 1 = 2.
# Update max_profit to the maximum of 6 and 2, which is 6.
# The loop ends, and the function returns max_profit, which is 6.

# Therefore, the solution correctly identifies that the maximum profit from buying on day 1 (price = 2) and selling on day 2 (price = 8) is 6.


# This solution has a time complexity of O(n), where n is the length of the prices array, as it only requires a single pass through the list. The space complexity is O(1) since it uses a constant amount of additional space.





