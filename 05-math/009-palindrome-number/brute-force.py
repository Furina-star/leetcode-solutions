"""
Palindrome Number - Brute Force Approach
Algorithm: String Conversion + Reversal Comparison
Time Complexity: O(log n)
Space Complexity: O(log n)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reversed_num = original[::-1]

        return original == reversed_num

def main():
    x = 12321

    solution = Solution()
    result = solution.isPalindrome(x)

    print(result)

if __name__ == "__main__":
    main()