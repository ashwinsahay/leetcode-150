prices = [2,4,1]

min_element=min(prices)
min_index=prices.index(min_element)

print(min_index)
print(max(prices[min_index+1:]))