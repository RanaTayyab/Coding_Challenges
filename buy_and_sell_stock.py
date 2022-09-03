def maxProfit(prices):
    minimum_rate = float('inf')

    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < minimum_rate:
            minimum_rate = prices[i]  # here we are fixing our left pointer in a variable which will always keep
            # updating minimum at any point in time, and will be having the lowest value to
            # subtract with in the future array values, and if difference of current array value
            # and by far minimum value we have, becomes greater than max profit, than store that max profit

        diff = prices[i] - minimum_rate

        if diff > max_profit:
            max_profit = diff

    return max_profit


maxProfit([7,1,5,3,6,4])