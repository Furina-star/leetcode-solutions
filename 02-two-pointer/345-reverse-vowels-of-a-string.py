"""
Reverse Vowels of a String
Algorithm: Two-Pointer Technique
Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        chars = list(s)  # strings are immutable, so swap in a list
        left = 0
        right = len(chars) - 1
        vowels = set("aeiouAEIOU")

        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return "".join(chars)


def main():
    s = "IceCreAm"

    solution = Solution()
    result = solution.reverseVowels(s)

    print(result)


if __name__ == "__main__":
    main()
