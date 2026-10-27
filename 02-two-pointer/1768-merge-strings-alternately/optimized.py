"""
Merge Strings Alternately - Optimized Approach
Algorithm: Two-Pointer Alternating Merge
Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = []

        while i < len(word1) or j < len(word2):

            if i < len(word1):
                result.append(word1[i])
                i += 1

            if j < len(word2):
                result.append(word2[j])
                j += 1

        final_result = "".join(result)

        return final_result

def main():
    word1 = "abc"
    word2 = "pqr"

    solution = Solution()
    result = solution.mergeAlternately(word1, word2)

    print(result)

if __name__ == "__main__":
    main()
