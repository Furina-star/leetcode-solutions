"""
Climbing Stairs.
Algorithm: Memoization Recursion
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def helper(x):
            if x <= 1:
                return 1

            if x in cache:
                return cache[x]

            cache[x] = helper(x - 1) + helper(x - 2)

            return cache[x]

        return helper(n)

def main():
    n = 2

    solution = Solution()
    result = solution.climbStairs(n)
    print(result)

if __name__ == "__main__":
    main()
