"""
Best Time to Buy and Sell Stock
Algorithm: Greedy Single-Pass
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for x in prices:
            if x < min_price:
                min_price = x

            profit = x - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit

def main():
    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()
    result = solution.maxProfit(prices)

    print(result)

if __name__ == "__main__":
    main()