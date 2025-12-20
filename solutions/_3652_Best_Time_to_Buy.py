class Solution:
    def createProfitSum(self, prices, len_prices, strategy):
        profitSum = [0] * len_prices
        i = 0
        for price, strategy_val in zip(prices, strategy):
            profitSum[i] = price*strategy_val
            i += 1

        for i in range(1, len_prices):
            profitSum[i] += profitSum[i-1]

        return profitSum

    def createPriceSum(self, prices, len_prices):
        priceSum = prices

        for i in range(1, len_prices):
            priceSum[i] += prices[i-1]

        return priceSum

    def maxProfit(self, prices, strategy, k):
        len_prices = len(prices)

        # Create profitSum -> prices[i] * strategy[i]
        profitSum = self.createProfitSum(prices, len_prices, strategy)

        # Create priceSum -> prices[i]
        priceSum = self.createPriceSum(prices, len_prices)

        max_profit = profitSum[len_prices-1]
        max_i = len_prices-k+1

        for i in range(max_i):

            sum_before_k = profitSum[i-1] if i != 0 else 0
            sum_in_k = priceSum[i+k-1] - priceSum[i+(k//2)-1]
            sum_after_k = profitSum[len_prices-1] - profitSum[i+k-1]

            temp = sum_before_k + sum_in_k + sum_after_k 

            if temp > max_profit:
                max_profit = temp

        return max_profit