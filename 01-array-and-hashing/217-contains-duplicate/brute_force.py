"""
Contains Duplicate - Brute Force Approach
Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range (i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False

def main():
    nums = [1, 2, 3 ,4]

    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()