"""
Valid Palindrome - Brute Force Approach
Algorithm: String Preprocessing + Reversal Comparison
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = s.lower()
        cleaned_text = "".join(char for char in text if char.isalnum())
        flipped = cleaned_text[::-1]
        if cleaned_text != flipped:
            return False
        return True

def main():
    s = "Was it a car or a cat I saw?"

    solution = Solution()
    result = solution.isPalindrome(s)
    print(result)

if __name__ == "__main__":
    main()