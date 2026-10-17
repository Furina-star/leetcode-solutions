
"""
Two Sum II - Brute Force Approach
Algorithm: Nested Loops
Time Complexity: O(n²)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int] | None:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]

        return None


def main():
    numbers = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    result = solution.twoSum(numbers, target)

    print(result)


if __name__ == "__main__":
    main()
