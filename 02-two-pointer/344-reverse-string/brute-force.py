"""
Reverse String - Brute Force Approach
Algorithm: Extra-List
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        reversed_chars = []

        for i in range(len(s) - 1, -1, -1):
            reversed_chars.append(s[i])

        for i in range(len(s)):
            s[i] = reversed_chars[i]


def main():
    s = ["A", "b", "C", "d"]

    solution = Solution()
    solution.reverseString(s)

    print(s)


if __name__ == "__main__":
    main()
