"""
Find Numbers with Even Number of Digits
Algorithm: Linear Scan
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        return sum(1 for d in nums if len(str(d)) % 2 == 0)

def main():
    nums = [12, 345, 2, 6, 7896]

    solution = Solution()
    result = solution.findNumbers(nums)

    print(result)

if __name__ == "__main__":
    main()