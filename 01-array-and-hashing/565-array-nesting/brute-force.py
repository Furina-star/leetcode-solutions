"""
Array Nesting - Brute-Force Approach
Algorithm: Repeated Cycle Traversal
Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        max_length = 0

        for start in range(len(nums)):
            visited = set()
            current = start
            length = 0

            while current not in visited:
                visited.add(current)
                current = nums[current]
                length += 1

            if length > max_length:
                max_length = length

        return max_length

def main():
    nums = [5, 4, 0, 3, 1, 6, 2]

    solution = Solution()
    result = solution.arrayNesting(nums)

    print(result)

if __name__ == "__main__":
    main()
