"""
Merge Strings Alternately - Brute Force Approach
Algorithm: Direct String Concatenation
Time Complexity: O((n+m)^2)
Space Complexity: O(n+m)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result = result + word1[i]

            if i < len(word2):
                result = result + word2[i]

        return result

def main():
    word1 = "abc"
    word2 = "pqr"

    solution = Solution()
    result = solution.mergeAlternately(word1, word2)

    print(result)

if __name__ == "__main__":
    main()
