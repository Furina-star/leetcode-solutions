"""
Can Place Flowers
Algorithm: Greedy with Single Traversal
Time Complexity: O(m)
Space Complexity: O(1)
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            current_plot = flowerbed[i]
            left_empty = i == 0 or flowerbed[i - 1] == 0
            right_empty = i == len(flowerbed) - 1 or flowerbed[i + 1] == 0

            if current_plot == 0 and left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1

                if n == 0:
                    return True

        return False


def main():
    flowerbed = [1,0,0,0,1]
    n = 1

    solution = Solution()
    result = solution.canPlaceFlowers(flowerbed, n)
    print(result)


if __name__ == "__main__":
    main()
