"""
First Unique Character in a String
Algorithm: Hash Map / Frequency Counting
Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequencies = Counter(s)
        for index, char in enumerate(s):
            if frequencies[char] == 1:
                return index

        return -1

def main():
    s = "aabbc"

    solution = Solution()
    result = solution.firstUniqChar(s)

    print(result)

if __name__ == "__main__":
    main()