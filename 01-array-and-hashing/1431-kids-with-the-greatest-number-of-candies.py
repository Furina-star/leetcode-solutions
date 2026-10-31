"""
Kids with the Greatest Number of Candies
Algorithm: Array Traversal / Precomputed Maximum
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result_bool = []

        for i in range(len(candies)):
            total_candies = candies[i] + extraCandies
            result_bool.append(total_candies >= max_candies)

        return result_bool


def main():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    solution = Solution()
    result = solution.kidsWithCandies(candies, extraCandies)

    print(result)


if __name__ == "__main__":
    main()
