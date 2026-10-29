
"""
1071. Greatest Common Divisor of Strings - Brute Force Approach
Algorithm: Descending Substring Enumeration + Repetition Checking
Time Complexity: O((n + m) * min(n, m))
Space Complexity: O(n + m)
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        for length in range(min(n, m), 0, -1):
            if n % length != 0 or m % length != 0:
                continue

            candidate = str1[:length]

            if (candidate * (n // length) == str1
                    and candidate * (m // length) == str2):
                return candidate

        return ""


def main():
    str1 = "ABABAB"
    str2 = "ABAB"

    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)

    print(result)


if __name__ == "__main__":
    main()
