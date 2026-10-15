"""
Ransom Note - Optimized Approach
Time complexity: O(m + n), where m is the length of magazine and n is the length of ransomNote
Space complexity: O(1)
"""
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequencies = Counter(magazine)
        for i in ransomNote:
            if frequencies[i] <= 0:
                return False

            frequencies[i] -= 1

        return True

def main():
    ransomNote = "a"
    magazine = "aab"

    solution = Solution()
    result = solution.canConstruct(ransomNote, magazine)

    print(result)

if __name__ == "__main__":
    main()