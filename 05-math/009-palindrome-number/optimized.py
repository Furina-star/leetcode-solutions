"""
Palindrome Number - Optimized Approach
Algorithm: Full Integer Reversal
Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome (self, x: int) -> bool:
        original = x
        reversed = 0

        while x > 0:
            digit = x % 10
            x = x // 10

            reversed = reversed * 10 + digit

        if reversed == original:
            return True

        return False

def main():
    x = 2147447412

    solution = Solution()
    result = solution.isPalindrome(x)

    print(result)

if __name__ == "__main__":
    main()