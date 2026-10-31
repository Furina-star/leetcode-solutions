"""
Valid Palindrome
Algorithm: Two-Pointer Technique
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if (ord(s[left]) | 32) != (ord(s[right]) | 32):
                return False

            left += 1
            right -= 1

        return True

def main():
    s = "race a car"

    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)

if __name__ == "__main__":
    main()