"""
Contains Duplicate - Optimized Approach
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

def main():
    nums = [1, 2, 3 ,1]

    solution = Solution()
    result = solution.containsDuplicate(nums)
    print(result)

if __name__ == "__main__":
    main()