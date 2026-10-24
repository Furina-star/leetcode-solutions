"""
Best Time to Buy and Sell Stock - Brute Force Approach
Algorithm: Exhaustive Search (Nested Loops)
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

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