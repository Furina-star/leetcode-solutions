"""
Richest Customer Wealth
Algrithm: Sum each customer's row, return the maximum total
Time complexity: O(m*n)
Space complexity: O(1)
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        return max(map(sum, accounts))


def main():
    accounts = [[1, 2, 3], [3, 2, 1]]

    solution = Solution()
    result = solution.maximumWealth(accounts)

    print(result)


if __name__ == "__main__":
    main()
