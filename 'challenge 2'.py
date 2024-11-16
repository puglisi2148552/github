'challenge 2'

def maximumToys(prices, k):
    toys = tot = 0
    prices.sort()
    for price in prices:
        tot += price
        if tot >k:
            break
        toys += 1
    return toys



