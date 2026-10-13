"""
Two Sum Problem - Brute Force Approach
Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

def main():

    #Input lists
    nums = [2,7,11,15]

    # Target sum
    target = 9

    # Calling
    solver = Solution()
    results = solver.twoSum(nums, target)

    print(results)

if __name__ == "__main__":
    main()