"""
1431. Kids With the Greatest Number of Candies
Approach: Brute Force
Algorithm: Nested Iteration
Time Complexity: O(n²)
Space Complexity: O(n)
"""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []

        for i in range(len(candies)):
            total_candies = candies[i] + extraCandies
            is_greatest = True

            for j in range(len(candies)):
                if total_candies < candies[j]:
                    is_greatest = False
                    break

            result.append(is_greatest)

        return result


def main():
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3

    solution = Solution()
    result = solution.kidsWithCandies(candies, extraCandies)

    print(result)


if __name__ == "__main__":
    main()
