"""
Two Sum II Input Array is Sorted
Algorithm: Two-Pointer Technique
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int] | None:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum > target:
                right -= 1

            elif current_sum < target:
                left += 1

            else:
                return[left + 1, right + 1]

        return None

def main():
    numbers = [-1,0]
    target = -1

    solution = Solution()

    result = solution.twoSum(numbers, target)
    print(result)

if __name__ == "__main__":
    main()