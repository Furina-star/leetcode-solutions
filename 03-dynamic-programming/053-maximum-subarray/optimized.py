"""
Maximum Subarray - Optimized Approach
Algorithm: Kadane's Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            current_sum = max(x, current_sum + x)

            max_sum = max(current_sum, max_sum)

        return max_sum

def main():
    nums = [5,4,-1,7,8]

    solution = Solution()
    result = solution.maxSubArray(nums)

    print(result)

if __name__ == "__main__":
    main()