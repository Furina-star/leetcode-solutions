"""
Greatest Common Divisor of Strings - Optimized Approach
Algorithm: String Concatenation Check + Euclidean Algorithm
Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        sliced_string = gcd(len(str1), len(str2))

        return str1[:sliced_string]


def main():
    str1 = "ABABAB"
    str2 = "ABAB"

    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)

    print(result)

if __name__ == "__main__":
    main()