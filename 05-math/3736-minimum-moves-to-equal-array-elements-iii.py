"""
Minimum Moves to Equal Array Elements III
Algorithm: Mathematical observation / greedy target selection
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        target = max(nums)
        total_moves = 0

        for num in nums:
            total_moves += target - num

        return total_moves


def main():
    nums = [2, 1, 3]

    solution = Solution()
    result = solution.minMoves(nums)

    print(result)


if __name__ == "__main__":
    main()
