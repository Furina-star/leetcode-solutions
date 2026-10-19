"""
Move Zeroes - Brute Force Approach
Algorithm: Backward Traversal with Removal and Append
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)

def main():
    nums = [0,0,0,3,12]

    solution = Solution()
    solution.moveZeroes(nums)

    print(nums)

if __name__ == "__main__":
    main()
