"""
Valid Anagram - Brute Force Approach
Algorithm: Linear Search / Character Removal
Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for char in s:
            if char not in t:
                return False
            t = t.replace(char, "", 1)

        return True


def main():
    s = "aabbc"
    t = "abcab"

    solution = Solution()
    result = solution.isAnagram(s, t)
    print(result)


if __name__ == "__main__":
    main()
