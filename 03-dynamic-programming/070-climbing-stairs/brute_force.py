"""
Climbing Stairs - Brute Force Approach.
Algorithm: Naive Recursion
Time Complexity: O(2^n)
Space Complexity: O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

def main():
    n = 2

    solution = Solution()
    result = solution.climbStairs(n)
    print(result)

if __name__ == "__main__":
    main()