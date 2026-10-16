"""
First Unique Character in a String - Brute Force Approach
Algorithm: Repeated Character Counting
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index, char in enumerate(s):
            if s.count(char) == 1:
                return index

        return -1

def main():
    s = "aaabbbc"

    solution = Solution()
    result = solution.firstUniqChar(s)

    print(result)

if __name__ == "__main__":
    main()
